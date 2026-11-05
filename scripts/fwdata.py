"""Load, validate and compile the Futures Watch data in this repo.

Every world, sci-fi future, question, signal, milestone and check is one YAML
file in its own folder. readings/<signal>.csv holds each signal's weekly
readings. tracker/ holds the weekly state: meta, calendar, update log and
probability history. build.py turns all of it into one data.json that the
static site reads.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WORLD_IDS = ["climb", "takeoff", "hangover", "fracture"]
SCIFI_IDS = ["utopia", "solarpunk", "singularity", "cyberpunk", "blackmirror", "dystopia", "collapse"]
LEANS = set(WORLD_IDS) | {"neutral"}
TRENDS = {"up", "down", "flat"}
TRACKING = {"active", "proposed"}
Q_DOMAINS = {"ai", "economy", "energy", "geopolitics", "politics", "tech", "education", "health"}
S_DOMAINS = {"ai", "jobs", "markets", "energy", "world", "politics", "tech", "education"}
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
URL_RE = re.compile(r"^https?://\S+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MONTH_RE = re.compile(r"^\d{4}-\d{2}(?:-\d{2})?$")
FOLDERS = ["worlds", "scifi", "questions", "signals", "milestones", "checks", "drivers"]
D_DOMAINS = {"tech", "economy", "geopolitics", "politics", "environment", "health"}
RESOLVES = {"yes", "partly", "no"}


def read_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def read_folder(name: str) -> list[dict]:
    out = []
    for p in sorted((ROOT / name).glob("*.yaml")):
        if p.name.startswith("_"):
            continue  # _template.yaml
        doc = read_yaml(p)
        if isinstance(doc, dict):
            doc["_file"] = p.stem
            out.append(doc)
        else:
            out.append({"_file": p.stem, "_bad": True})
    return out


def read_readings() -> dict[str, list[dict]]:
    out = {}
    for p in sorted((ROOT / "readings").glob("*.csv")):
        with p.open(encoding="utf-8", newline="") as f:
            rows = []
            for r in csv.DictReader(f):
                n = (r.get("num") or "").strip()
                try:
                    num = float(n) if n else None
                except ValueError:
                    num = "bad"
                if isinstance(num, float) and num.is_integer():
                    num = int(num)
                rows.append({"date": r.get("date") or "", "asOf": r.get("asOf") or "", "value": r.get("value") or "",
                             "num": num, "unit": r.get("unit") or None})
        out[p.stem] = rows
    return out


def load_all() -> dict:
    data = {name: read_folder(name) for name in FOLDERS}
    tr = ROOT / "tracker"
    data["meta"] = read_yaml(tr / "meta.yaml") or {}
    data["calendar"] = read_yaml(tr / "calendar.yaml") or []
    data["updates"] = [read_yaml(p) for p in sorted((tr / "updates").glob("*.yaml"), reverse=True)]
    data["history"] = [json.loads(p.read_text(encoding="utf-8")) for p in sorted((tr / "history").glob("*.json"))]
    data["readings"] = read_readings()
    return data


# ---------------------------------------------------------------- validation

def _int(v, lo=None, hi=None):
    return isinstance(v, int) and not isinstance(v, bool) and (lo is None or v >= lo) and (hi is None or v <= hi)


def _text(d, k):
    return isinstance(d.get(k), str) and d[k].strip() != ""


def _url_ok(u):
    return u is None or (isinstance(u, str) and URL_RE.match(u))


def _check_id(d, errs, where):
    if d.get("_bad"):
        errs.append(f"{where}: file must be a YAML mapping"); return False
    if d.get("id") != d["_file"] or not ID_RE.match(str(d.get("id"))):
        errs.append(f"{where}: id must match the file name, lowercase-with-dashes")
    if not _int(d.get("order"), 1):
        errs.append(f"{where}: order must be a whole number from 1")
    return True


def _check_prob(d, errs, where, name="prob"):
    if not _int(d.get(name), 0, 100):
        errs.append(f"{where}: {name} must be a whole number 0-100")
    if d.get("prevProb") is not None and not _int(d["prevProb"], 0, 100):
        errs.append(f"{where}: prevProb must be a whole number 0-100 or empty")


def _sum100(items, errs, where):
    vals = [i.get("prob") for i in items]
    if all(_int(v) for v in vals) and sum(vals) != 100:
        errs.append(f"{where}: odds add up to {sum(vals)}, not 100")


def validate(data: dict) -> list[str]:
    errs: list[str] = []
    qids = {q["_file"] for q in data["questions"]}
    sids = {s["_file"] for s in data["signals"]}

    for group, ids, label in (("worlds", WORLD_IDS, "world"), ("scifi", SCIFI_IDS, "sci-fi future")):
        docs = data[group]
        have = {d["_file"] for d in docs}
        if have != set(ids):
            errs.append(f"{group}/: expected exactly these files: {', '.join(i + '.yaml' for i in ids)}")
        for d in docs:
            w = f"{group}/{d['_file']}.yaml"
            if not _check_id(d, errs, w):
                continue
            _check_prob(d, errs, w)
            for k in ("name", "tagline", "summary"):
                if not _text(d, k):
                    errs.append(f"{w}: '{k}' is required")
        _sum100(docs, errs, f"{group}/ ({label} odds)")
    for d in data["scifi"]:
        for q in d.get("drivers") or []:
            if q not in qids:
                errs.append(f"scifi/{d['_file']}.yaml: driver '{q}' is not a file in questions/")

    for q in data["questions"]:
        w = f"questions/{q['_file']}.yaml"
        if not _check_id(q, errs, w):
            continue
        for k in ("title", "short", "read"):
            if not _text(q, k):
                errs.append(f"{w}: '{k}' is required")
        if q.get("domain") not in Q_DOMAINS:
            errs.append(f"{w}: domain must be one of {', '.join(sorted(Q_DOMAINS))}")
        if q.get("tracking") not in TRACKING:
            errs.append(f"{w}: tracking must be 'active' or 'proposed'")
        ocs = q.get("outcomes")
        if not isinstance(ocs, list) or len(ocs) < 2:
            errs.append(f"{w}: needs at least two outcomes")
        else:
            keys = set()
            for i, o in enumerate(ocs):
                ow = f"{w} outcome {i + 1}"
                if not isinstance(o, dict):
                    errs.append(f"{ow}: must be a mapping"); continue
                if not ID_RE.match(str(o.get("key"))) or o.get("key") in keys:
                    errs.append(f"{ow}: key must be unique and lowercase-with-dashes")
                keys.add(o.get("key"))
                for k in ("label", "desc"):
                    if not _text(o, k):
                        errs.append(f"{ow}: '{k}' is required")
                _check_prob(o, errs, ow)
            _sum100(ocs, errs, w)
        anchors = q.get("anchors") or []
        if q.get("tracking") == "active" and len(anchors) < 1:
            errs.append(f"{w}: an active question needs at least one anchor")
        for i, a in enumerate(anchors):
            aw = f"{w} anchor {i + 1}"
            if not isinstance(a, dict) or not _text(a, "who") or not _text(a, "what"):
                errs.append(f"{aw}: needs 'who' and 'what'"); continue
            if not _url_ok(a.get("url")):
                errs.append(f"{aw}: url must be an http(s) link (leave it empty only for a base rate)")
            if a.get("date") and not MONTH_RE.match(str(a["date"])):
                errs.append(f"{aw}: date must be YYYY-MM")
        for s in q.get("signals") or []:
            if s not in sids:
                errs.append(f"{w}: signal '{s}' is not a file in signals/")

    for s in data["signals"]:
        w = f"signals/{s['_file']}.yaml"
        if not _check_id(s, errs, w):
            continue
        for k in ("name", "measures", "value", "watch", "cadence", "source"):
            if not _text(s, k):
                errs.append(f"{w}: '{k}' is required")
        if s.get("domain") not in S_DOMAINS:
            errs.append(f"{w}: domain must be one of {', '.join(sorted(S_DOMAINS))}")
        if s.get("tracking") not in TRACKING:
            errs.append(f"{w}: tracking must be 'active' or 'proposed'")
        if s.get("leans") not in LEANS:
            errs.append(f"{w}: leans must be one of {', '.join(sorted(LEANS))}")
        if s.get("trend") not in TRENDS:
            errs.append(f"{w}: trend must be up, down or flat")
        if not MONTH_RE.match(str(s.get("asOf") or "")):
            errs.append(f"{w}: asOf must be YYYY-MM-DD or YYYY-MM")
        if not s.get("url") or not _url_ok(s.get("url")):
            errs.append(f"{w}: needs an http(s) url to the source")

    for name in ("milestones", "checks"):
        for m in data[name]:
            w = f"{name}/{m['_file']}.yaml"
            if not _check_id(m, errs, w):
                continue
            _check_prob(m, errs, w)
            for k in ("label", "note", "source"):
                if not _text(m, k):
                    errs.append(f"{w}: '{k}' is required")
            if not _url_ok(m.get("url")):
                errs.append(f"{w}: url must be an http(s) link")
            if name == "checks":
                if not DATE_RE.match(str(m.get("resolvesBy") or "")):
                    errs.append(f"{w}: resolvesBy must be YYYY-MM-DD")
                if m.get("resolved") not in (None, "yes", "no"):
                    errs.append(f"{w}: resolved must be empty, 'yes' or 'no'")
                elif m.get("resolved") and m.get("prob") != (100 if m["resolved"] == "yes" else 0):
                    errs.append(f"{w}: a resolved check needs prob 100 (yes) or 0 (no)")

    for sig, rows in data["readings"].items():
        w = f"readings/{sig}.csv"
        if sig not in sids:
            errs.append(f"{w}: no signal file signals/{sig}.yaml")
        dates = [r["date"] for r in rows]
        if len(set(dates)) != len(dates):
            errs.append(f"{w}: each date may appear once")
        for r in rows:
            if not DATE_RE.match(r["date"]):
                errs.append(f"{w}: bad date '{r['date']}'")
            if r["num"] == "bad":
                errs.append(f"{w} {r['date']}: num must be a number or empty")

    dids = {d["_file"] for d in data["drivers"]}
    for d in data["drivers"]:
        w = f"drivers/{d['_file']}.yaml"
        if d.get("_bad"):
            errs.append(f"{w}: file must be a YAML mapping"); continue
        if d.get("id") != d["_file"] or not ID_RE.match(str(d.get("id"))):
            errs.append(f"{w}: id must match the file name, lowercase-with-dashes")
        for k in ("name", "question", "impact_why", "uncertainty_why"):
            if not _text(d, k):
                errs.append(f"{w}: '{k}' is required")
        if d.get("domain") not in D_DOMAINS:
            errs.append(f"{w}: domain must be one of {', '.join(sorted(D_DOMAINS))}")
        for k in ("impact", "uncertainty"):
            if not _int(d.get(k), 1, 5):
                errs.append(f"{w}: {k} must be a whole number 1-5")
        if d.get("resolves_by_2029") not in RESOLVES:
            errs.append(f"{w}: resolves_by_2029 must be yes, partly or no")
        if not isinstance(d.get("poles"), list) or len(d["poles"]) != 2:
            errs.append(f"{w}: poles needs exactly two outcomes")
        for c in d.get("correlated_with") or []:
            if not isinstance(c, dict) or c.get("id") not in dids:
                errs.append(f"{w}: correlated_with entries need an id that is a file in drivers/")
        srcs = d.get("sources") or []
        if not srcs:
            errs.append(f"{w}: needs at least one source")
        for s in srcs:
            if not isinstance(s, dict) or not s.get("url") or not _url_ok(s.get("url")):
                errs.append(f"{w}: every source needs an http(s) url")

    seen = set()
    for i, e in enumerate(data["calendar"]):
        w = f"tracker/calendar.yaml entry {i + 1}"
        if not isinstance(e, dict):
            errs.append(f"{w}: must be a mapping"); continue
        if e.get("id") in seen or not ID_RE.match(str(e.get("id"))):
            errs.append(f"{w}: id must be unique, like 2026-11-06-jobs")
        seen.add(e.get("id"))
        if not DATE_RE.match(str(e.get("date") or "")):
            errs.append(f"{w}: date must be YYYY-MM-DD")
        if not _text(e, "event"):
            errs.append(f"{w}: 'event' is required")
        if not _url_ok(e.get("url")):
            errs.append(f"{w}: url must be an http(s) link")

    m = data["meta"]
    for k in ("title", "repo", "horizon", "updatedAt", "nextUpdate", "headline"):
        if not _text(m, k) and not (k in ("horizon", "updatedAt", "nextUpdate") and m.get(k)):
            errs.append(f"tracker/meta.yaml: '{k}' is required")
    if not _int(m.get("week"), 0):
        errs.append("tracker/meta.yaml: week must be a whole number")
    for u in data["updates"]:
        if not isinstance(u, dict) or not DATE_RE.match(str(u.get("date") or "")):
            errs.append("tracker/updates/: every update needs a YYYY-MM-DD date")
    for h in data["history"]:
        if not isinstance(h, dict) or not isinstance(h.get("worlds"), dict):
            errs.append("tracker/history/: every snapshot needs date and worlds")
    return errs


# ------------------------------------------------------------------ compile

def _clean(d: dict, folder: str) -> dict:
    out = {k: v for k, v in d.items() if not k.startswith("_")}
    out["file"] = f"{folder}/{d['_file']}.yaml"
    return out


def compile_site(data: dict) -> dict:
    by_order = lambda d: (d.get("order", 999), d.get("id", ""))
    site = {name: sorted((_clean(d, name) for d in data[name]), key=by_order) for name in FOLDERS}
    site["meta"] = data["meta"]
    site["calendar"] = sorted(data["calendar"], key=lambda e: (str(e.get("date")), e.get("id", "")))
    site["updates"] = data["updates"]
    site["history"] = data["history"]
    site["readings"] = {k: [{kk: vv for kk, vv in r.items() if vv not in (None, "")} for r in rows]
                        for k, rows in data["readings"].items()}
    return site
