# Contributing

Thanks for helping. The most useful contributions are:

- **A new signal**: a data series, market or benchmark that would tell us which world we're heading into.
- **A new forecast anchor**: a market, expert or published estimate a what-if should be checked against.
- **A correction**: a stale reading, a wrong fact or a dead link, with a source.
- **A new question**: something you wonder about the next few years, like what happens to a job, a price or a technology.

Every change is a pull request. The checks run `python scripts/validate.py`, and the weekly review folds accepted proposals in. You don't need to set or change any odds. Proposals don't move numbers until the review makes them active.

Not comfortable editing files? [Suggest a factor](../../issues/new?template=suggest-a-factor.yml) or [report a correction](../../issues/new?template=correction.yml) instead.

## Add a signal

1. Pick an id: lowercase words joined by dashes, like `ev-share` or `chip-exports`. It becomes the file name and the page address.
2. Copy `signals/_template.yaml` to `signals/<id>.yaml` and fill it in (field guide below). Leave `tracking: proposed`.
3. Optionally, add the id to the `signals:` list of each what-if in `questions/` it informs.
4. Run `python scripts/validate.py` and fix anything it reports.
5. Open a pull request saying which world or what-if the signal tells us about, and why.

A good signal is **published on a schedule**, **comes from a primary source** and has a **threshold** that would clearly change the odds. "Brent above $130 for weeks points to Fracture" is a signal. "Vibes in tech" is not.

## Add a forecast anchor

Add an entry to the `anchors:` list in `questions/<id>.yaml`:

```yaml
- who: Metaculus forecasters
  what: Median for the first general AI system is February 2031.
  date: 2026-10
  url: https://www.metaculus.com/questions/5121/
```

Keep about seven anchors per question. If you add one past that, say which it replaces.

## Add a what-if

Copy `questions/_template.yaml` to `questions/<id>.yaml`. Give it two to four mutually exclusive outcomes whose `prob` values sum to 100, and at least one anchor. Your starting odds are a proposal; the review sets them from the anchors and base rates. Leave `tracking: proposed`.

## What makes a good source

Prefer, in roughly this order: official statistics (BLS, BEA, Fed, EIA, Copernicus, NOAA, WHO), regulators and courts, liquid prediction markets (Kalshi, Polymarket), forecasting platforms (Metaculus, Manifold), peer-reviewed research and established evaluators (METR, Epoch AI, ARC Prize), company filings, then major news outlets. Link the page that actually states the number. Avoid blogs, forums and anything selling something.

Report political, election and market odds neutrally. No opinions, and no favoring a party.

## Field guide: signals/<id>.yaml

| Field | What it means |
|---|---|
| `id` | Same as the file name. |
| `tracking` | `proposed` for new signals. The weekly review switches it to `active`. |
| `name` | Short display name, like `Oil price (Brent)`. |
| `domain` | `ai`, `jobs`, `markets`, `energy`, `world`, `politics`, `tech`, `education`, `health`, `home` or `creative`. |
| `order` | Position in the list. Use the next free number. |
| `measures` | One sentence on what the number is. |
| `value` | The latest reading as text, like `4.3%` or `≈$106`. |
| `asOf` | When the data is from: `YYYY-MM-DD` or `YYYY-MM`. |
| `trend` | `up`, `down` or `flat`. |
| `leans` | Which world the current reading supports: `climb`, `takeoff`, `hangover`, `fracture` or `neutral`. |
| `note` | One or two sentences of context for the latest reading. |
| `watch` | The threshold that would change the odds, and which way. |
| `cadence` | How often the source updates, like `Monthly (first Friday)`. |
| `source`, `url` | Who publishes it, and a link to the page with the number. |

## Field guide: questions/<id>.yaml

| Field | What it means |
|---|---|
| `id`, `tracking`, `order` | As above. |
| `title` | A plain, open question a reader would ask, such as "What happens to home prices?". Every outcome's `says` should read as an answer to it. |
| `short` | One sentence on what's being forecast, by the end of 2029. |
| `domain` | `ai`, `economy`, `energy`, `geopolitics`, `politics`, `tech`, `education` or `health`. |
| `area` | The life area it is grouped under on the site: `ai` (AI itself), `work` (work and learning), `money` (money and home), `health`, `tech` (everyday tech and energy) or `world`. |
| `read` | Two sentences: the current state of the evidence. |
| `outcomes` | 2–4 entries of `key`, `label` (a short name for charts), `says` (a plain sentence under about 60 characters that answers the title, shown on the home page card), `prob`, `prevProb`, `desc` (what the outcome is) and `ifThen` (what it would mean). `prob` values sum to 100. |
| `anchors` | Forecasts this question rests on: `who`, `what`, `date` (`YYYY-MM`), `url`. Leave `url` empty only for a historical base rate. |
| `signals` | Ids of signals that move it. |

## Files the weekly review maintains

`worlds/`, `scifi/`, `milestones/`, `checks/`, `readings/` and `tracker/` are updated by the weekly review. Corrections to them are welcome, but please don't change odds directly. Open an issue or say in your pull request what you think should move and why.

## Style

Plain, specific, active voice, short sentences. Paraphrase sources; no quote longer than 15 words. Keep each text field about as long as what it replaces.
