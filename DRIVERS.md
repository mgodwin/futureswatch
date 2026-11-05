# Drivers: choosing what the worlds are built from

The four worlds should come from the forces most likely to define the years to the end of 2029, not from a guess. This file is how we pick them, using a standard scenario-planning method:

1. List every candidate driver broadly: technology, economy, geopolitics, politics, environment, health.
2. Score each one 1 to 5 on **impact** (how much its plausible range of outcomes would change everyday life and the economy in major economies by 2029) and **uncertainty** (how split informed forecasts are on which way it goes; 1 means the direction is near-certain, which makes it background rather than a decider).
3. Pick the **two** drivers that score high on both and are roughly **independent** of each other.
4. Cross them into a 2×2. The four combinations are the worlds. Everything else becomes a variable that plays out inside each world.

Each driver is one file in [`drivers/`](drivers/), with its question, its two poles, both scores with the evidence behind them, what it is correlated with, which repo files already track it, and sources. The first scoring was done on 2026-11-04. Several figures rest on secondary or undated sources, marked in each file; corrections are welcome.

## The ranking

| Score | Impact × uncertainty | Driver | Resolves by 2029 |
|---:|:---:|---|---|
| 25 | 5 × 5 | [AI capability trajectory](drivers/ai-capability.yaml) | partly |
| 25 | 5 × 5 | [AI investment cycle and financial stability](drivers/ai-investment-cycle.yaml) | yes |
| 20 | 5 × 4 | [AI diffusion into work](drivers/ai-diffusion.yaml) | partly |
| 16 | 4 × 4 | [AI control and governance](drivers/ai-control.yaml) | partly |
| 16 | 4 × 4 | [Middle East war and oil shocks](drivers/middle-east-energy.yaml) | partly |
| 16 | 4 × 4 | [US institutional stability](drivers/us-institutions.yaml) | yes |
| 15 | 5 × 3 | [US-China rivalry and Taiwan](drivers/us-china-taiwan.yaml) | partly |
| 15 | 5 × 3 | [World order: stable or fractured](drivers/world-order.yaml) | partly |
| 12 | 4 × 3 | [Energy and compute supply](drivers/energy-compute.yaml) | yes |
| 12 | 4 × 3 | [US fiscal path, inflation and rates](drivers/us-fiscal-inflation.yaml) | partly |
| 9 | 3 × 3 | [Trade fragmentation](drivers/trade-fragmentation.yaml) | partly |
| 9 | 3 × 3 | [Russia, Ukraine and European security](drivers/russia-europe.yaml) | partly |
| 9 | 3 × 3 | [Global democracy and populism](drivers/global-democracy.yaml) | partly |
| 8 | 4 × 2 | [Pandemic and biosecurity](drivers/pandemic-biosecurity.yaml) | yes |
| 6 | 3 × 2 | [Biotech and medical breakthroughs](drivers/biotech.yaml) | partly |
| 6 | 3 × 2 | [Information ecosystem and trust](drivers/info-trust.yaml) | partly |
| 6 | 3 × 2 | [China's economic trajectory](drivers/china-economy.yaml) | partly |
| 6 | 3 × 2 | [Demographics and labor supply](drivers/demographics.yaml) | no |
| 6 | 3 × 2 | [Nuclear use, testing and proliferation](drivers/nuclear-risk.yaml) | no |
| 6 | 3 × 2 | [Climate impacts and extreme events](drivers/climate-impacts.yaml) | partly |

What the scores say:

- **AI dominates the top**, but the top three AI drivers move together. Capex is only justified if capability keeps climbing, and diffusion depends on both. Crossing two of them would produce quadrants that barely happen (transformative AI with a deep bust, a plateau with a sustained boom).
- **Outside AI, three drivers score well and are mostly independent of it:** US institutional stability, world order and the Middle East. World order works better as one axis than its parts (Taiwan, Ukraine, the Gulf, nuclear risk), because each part alone is either a low-probability tail or moderate in impact.
- **Background, not deciders:** demographics, climate, China's economy, biotech, nuclear risk and the information ecosystem. Each is important, but its direction by 2029 is fairly clear or its big outcome is a low-probability tail. They stay tracked as what-ifs and signals inside the worlds.

## Candidate axis pairs

### A. AI payoff × world order (leading candidate)

Merge the two correlated top scorers into one axis, **AI payoff**: does AI deliver (capability keeps climbing and the investment pays off) or disappoint (progress stalls short of experts and the boom corrects or busts)? Cross it with **world order**: does the system bend but hold, or fracture into blocs with a defining war?

| | Order holds | Order fractures |
|---|---|---|
| **AI delivers** | AI-led boom in a stable world | AI race in a fractured world |
| **AI disappoints** | AI bust or slow muddle in a stable world | Fractured world without the AI payoff |

Covers the two highest-impact domains and is global rather than US-only. The catch: the current Steady Climb and Takeoff would merge into the top-left quadrant, unless "delivers" is split further or kept as a variable inside it.

### B. AI payoff × US institutional stability

The same AI axis crossed with whether US institutions hold through the 2028 election and transfer. Resolves cleanly by January 2029 and is only loosely tied to AI. The catch: it is US-centric again, and it leaves war and oil shocks as variables inside each world.

### C. AI capability × AI investment cycle (rejected)

The two highest raw scores, but they are strongly correlated, so two of the four quadrants would be near-empty. Shown here because it is the obvious pairing from the table alone.

## Next steps

1. Pick an axis pair, or score more drivers together without a 2×2 (draft in [FRAME.md](FRAME.md)).
2. Set each axis's cut point near 50/50 using the anchors, so all four quadrants are real.
3. Rewrite `worlds/`, `METHODOLOGY.md` and the weekly prompt for the new frame, and map the old history onto it where it translates.

Disagree with a score? Open a pull request on the driver's file with your evidence, or [suggest a factor](../../issues/new?template=suggest-a-factor.yml).
