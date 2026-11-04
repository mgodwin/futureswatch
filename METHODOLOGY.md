# Methodology

Futures Watch forecasts how the period from now to **December 31, 2029** will be defined. The odds are judgment calls anchored to markets, published forecasts and base rates, and they move only on evidence.

## The four worlds

The worlds are mutually exclusive and their odds always sum to 100. A period is classified in priority order:

1. **Fracture**: a war or pandemic shock dominates the period. That means a Taiwan blockade or war, a NATO–Russia war, a regional Gulf war, a pandemic that kills over a million people, or nuclear use. Overlap between these is allowed for.
2. **Takeoff**: otherwise, transformative AI arrives. As a guide, Takeoff ≈ P(`ai-capability` = transformative) × (1 − Fracture).
3. **Hangover**: otherwise, an AI bust (`ai-boom` = bust) or a recession defines the period.
4. **Steady Climb**: everything else.

After each re-score these relationships should hold within about 3 points. The Takeoff formula is a guide, not a rule. When Fracture rises for a reason that would not slow AI progress (a Gulf war, say), Takeoff can hold and the point comes from Steady Climb or Hangover. When the reason could speed an AI race (a Taiwan crisis), the change says so. Any deviation is explained in the change's `why`.

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
