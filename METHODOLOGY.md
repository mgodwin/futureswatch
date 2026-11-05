# Methodology

Futures Watch tracks what the years to **December 31, 2029** are most likely to look like: for AI itself, work, money and home, health, everyday tech and the wider world. The odds are judgment calls anchored to markets, published forecasts and base rates, and they move only on evidence.

## Questions

The core of the site is a set of separate questions, like "What happens to software engineers?" or "Will home prices hold?". Each has two to four mutually exclusive outcomes whose odds sum to 100, the forecasts they're anchored to, and the signals that would move them. Questions are grouped by life area, and each one stands on its own: you can read the housing question without accepting anything about the worlds below.

Questions that depend on each other are kept consistent (see the list at the end of the worlds section), but nothing assumes they move together unless the evidence says so.

## Focus

Each question shows how settled its odds are, from 0 (every outcome equally likely) to 100 (one outcome certain). The number is one minus the normalized Shannon entropy of the outcome odds, so questions with two, three or four outcomes compare fairly. It is recorded in the data with each question's weekly history, in four bands: wide open (under 15), leaning (15 to 39), fairly clear (40 to 64) and clear (65 and up), so the weekly update can say when a question is getting clearer. The home page cards don't show it; they show the most likely outcome and its odds.

Focus measures how lopsided the odds are, not how good the evidence is. A question can be clear because the base rate is lopsided (most years don't bring a pandemic), not because anyone has special insight.

## Most likely 2030

The portrait in `tracker/portrait.yaml` puts the leading outcome of each question into a few plain paragraphs, one per life area. It is rewritten when the leading outcomes change. It states clear questions plainly and marks wide-open ones as open.

With many separate questions, the exact combination of every leading outcome is itself unlikely, even when each piece is the single best bet. The portrait is "the most likely answer to each question", not a prediction that all of them come true together.

## The four worlds

The worlds are a summary layer: a short answer to "which kind of period is this?" They are mutually exclusive and their odds always sum to 100. A period is classified in priority order:

1. **Fracture**: a war or pandemic shock dominates the period. That means a Taiwan blockade or war, a NATO–Russia war, a regional Gulf war, a pandemic that kills over a million people, or nuclear use. Overlap between these is allowed for.
2. **Takeoff**: otherwise, transformative AI arrives. Takeoff is the chance of transformative AI *and* no Fracture. That equals P(`ai-capability` = transformative) × (1 − Fracture) only if the two are independent, and they aren't quite: a Taiwan shock would cut chip supply, while a race could speed AI up.
3. **Hangover**: otherwise, an AI bust (`ai-boom` = bust) or a recession defines the period.
4. **Steady Climb**: everything else.

After each re-score these relationships should hold within about 3 points. The product is a starting point, not a rule. When Fracture rises for a reason that would not slow AI progress (a Gulf war, say), Takeoff can hold and the point comes from Steady Climb or Hangover. When the reason could speed an AI race (a Taiwan crisis), the change says so. Any deviation is explained in the change's `why`.

Some questions don't feed the worlds directly but must stay consistent with others:

- A Major or Systemic `ai-cyber` outcome moves `ai-control` toward Emergency brakes.
- A China AI lead in `us-china-ai` is weighed in `taiwan` and `ai-control`.
- `higher-ed` stays consistent with `ai-jobs`: a Mass disruption jobs path makes Squeezed or Unbundled more likely.

## The sci-fi lens

The same evidence, read as fiction: which story would the world at the end of 2029 most resemble? The seven futures sum to 100 and are classified in priority order:

| Future | Defined by | Weighed against |
|---|---|---|
| Collapse | A catastrophe breaks basic systems across a major region | Nuclear use, a pandemic over 1M deaths with breakdown, a NATO–Russia or US–China war. Stays well below Fracture. |
| Singularity | AI systems do most research and key decisions | A slice of Takeoff; `ai-capability` transformative, `ai-control` open |
| Dystopia | Emergency powers and mass surveillance define life in major countries | `ai-control` brakes, `gulf` regional, `taiwan` blockade, new surveillance or emergency-power laws |
| Utopia | Transformative AI with broadly shared gains | A slice of Takeoff; `ai-control` managed, `ai-jobs` not mass |
| Solarpunk | Clean energy and climate progress define the period | `climate` below, `power-grid` keeps up, `fusion` |
| Cyberpunk | Tech races ahead while gains concentrate and work grows precarious | `ai-boom` sustained, `ai-jobs` absorbed or mass, `ai-cyber` major, AI market concentration |
| Black Mirror | The rest: life mostly familiar, unsettling tech at the edges | Close to Steady Climb |

No market prices these, so a sci-fi future may move 2 or more points only when its `drivers` questions moved that way the same week.

## How odds move

**Evidence rule.** An outcome may move 2 or more points in a week only if:

- (a) a cited forecasting market or published forecast moved the same way, or
- (b) a discrete event crossed a signal's `watch` threshold.

The change's `why` names which one. Otherwise a move is capped at 1 point, or the odds stay put.

**Weekly cap.** No outcome moves more than 5 points in a week unless a major discrete event happened, and the log says so explicitly. An election result counts as a major discrete event for `us-power`.

**Drift check.** If a world or sci-fi future has moved the same direction three updates in a row (see `tracker/history/`), it is re-checked against the anchors before moving again, and the week's write-up says whether the anchors support the trend.

**Integers that sum to 100.** Every world set, sci-fi set and question's outcomes are whole numbers that sum to exactly 100. `prevProb` holds last week's value so the site can show the change, including "no change".

## Signals

Each signal has a current `value`, the date the data is `asOf`, a `trend`, the world it currently `leans` toward and a `watch` threshold that would change the odds.

- Every week each signal's own source is checked for a release since its `asOf` date.
- **Stale-signal rule:** a signal whose `asOf` is more than 90 days old gets an active search for a newer reading. If its source has stopped updating, it is replaced with the best live source under the same id, and the note says so.
- Every run appends one row per signal to `readings/<id>.csv`, changed or not. `num` is the single headline number the value states, in the same `unit` as the previous row, or empty when the value isn't numeric. No number is computed that the source doesn't give, except a simple sum or midpoint the value itself shows.

## Short-range checks

Checks in `checks/` resolve within one to six months, ideally with a liquid market price. They keep the forecast honest long before 2030.

- Unresolved checks are re-scored from their cited market each week. Three to six stay live.
- When one resolves (the event happens, or `resolvesBy` passes): `prevProb` keeps the last forecast, `prob` becomes 100 or 0, `resolved` becomes `yes` or `no`, and the note starts "Resolved yes/no on <date>; last forecast X%".
- The resolution is appended to `tracker/meta.yaml` `scorecard` with its Brier score, (forecast/100 − outcome)², rounded to 3 decimals. 0 is perfect and 0.25 is what always saying 50% would earn.
- Resolved checks stay in place as the track record.

## Contributor proposals

Signals and questions added by contributors start with `tracking: proposed`. The weekly review verifies their sources, adds a first reading or sets starting odds from anchors and base rates, and links them in. Then it sets `tracking: active`. Proposals don't move any odds until they are active.

## Limits

Some markets cited here trade thinly. Some figures come from secondary reports, and lab-reported benchmarks are not independently verified. Political, election and market odds are reported neutrally.
