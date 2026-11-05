# Frame draft: scored combinations instead of a 2×2

Status: draft, first estimate on 2026-11-05. Nothing on the site uses this yet.

[DRIVERS.md](DRIVERS.md) ranks the forces most likely to define the years to the end of 2029. A 2×2 would keep only two of them. This draft keeps three and scores every combination directly, so drivers that move together are handled in the odds rather than assumed away.

## The three drivers

Each one is chosen to be high impact, genuinely uncertain, and mostly independent of the other two. Each has states that can be checked by the end of 2029.

**AI payoff** (merges [AI capability](drivers/ai-capability.yaml) and the [AI investment cycle](drivers/ai-investment-cycle.yaml), which move together)

| State | Resolves as | Odds |
|---|---|---:|
| Pays off | Transformative AI (as defined in [the capability question](questions/ai-capability.yaml)), or the build-out is sustained through 2029 with no deep bust | 40 |
| Muddles | Powerful but jagged AI, and any correction recovers without a recession | 35 |
| Busts | The unwind feeds a recession, with losses on data-center debt | 25 |

This axis has three states, not two. With two, "falls short" would lump a soft landing together with a bust, and the biggest cell would hide the difference between Steady Climb and Hangover that the site tracks today.

**[World order](drivers/world-order.yaml)**

| State | Resolves as | Odds |
|---|---|---:|
| Holds | None of the events below | 70 |
| Fractures | A Taiwan blockade or war, a NATO–Russia war, a regional Gulf war with oil above $150 for months, a pandemic that kills over a million people, or any nuclear use | 30 |

Combining the current question odds as if they were independent gives about 33%. Positive links between them pull that down, so this draft uses 30. That is well above the 20% the Fracture world shows today, which the first weekly update under this frame would have to reconcile.

**[US institutions](drivers/us-institutions.yaml)**

| State | Resolves as | Odds |
|---|---|---:|
| Holds | The 2028 result is accepted and transferred normally, with courts and Congress working as checks | 75 |
| Strains | A contested transfer, emergency powers at home or open defiance of courts | 25 |

Anchored on the Manifold market's 75% for a normal transfer.

## Links between drivers

Only links with a clear mechanism get an adjustment. Everything else is treated as independent.

- **Fracture makes a US crisis likelier.** Strain is 35% in a fractured world and 21% in a stable one (25% overall). War powers, emergency measures and a rally-or-backlash election all raise the risk.
- **Fracture hurts the AI payoff.** A Taiwan shock cuts chip supply and an oil or war shock tips recession, so in a fractured world the odds are 33 pays off / 35 muddles / 32 busts, against 43 / 35 / 22 in a stable one.
- **US institutions and AI payoff** are treated as independent for now. A mass-layoff shock feeding political strain is a plausible link, but no data supports it yet.

## The twelve combinations

| World order | US institutions | AI pays off | AI muddles | AI busts | Row |
|---|---|---:|---:|---:|---:|
| Holds | Holds | **24** | **20** | **12** | 56 |
| Holds | Strains | 6 | 5 | 3 | 14 |
| Fractures | Holds | 6 | 7 | 6 | 19 |
| Fractures | Strains | 4 | 4 | 3 | 11 |

The cells add to 100 and match each driver's own odds above, within rounding.

## How they read as worlds

The three biggest cells are distinct enough to name on their own. The rest group by the driver that would define the period.

| World | Cells | Odds | Today's frame |
|---|---|---:|---|
| **Takeoff** | AI pays off, order holds, US holds | 24 | Takeoff 24 |
| **Steady Climb** | AI muddles, order holds, US holds | 20 | Steady Climb 32 |
| **Hangover** | AI busts, order holds, US holds | 12 | Hangover 24 |
| **Fracture** | Every cell where order fractures | 30 | Fracture 20 |
| **American crisis** (new) | Order holds, US strains | 14 | none |

Each grouped world still shows its AI split, because it changes what the world means: Fracture is 10 pays off / 11 muddles / 9 busts, and American crisis is 6 / 5 / 3.

What this changes compared with today:

- **A fifth world appears.** A contested 2028 transfer in an otherwise stable world was hidden inside Steady Climb. At 14% it is bigger than Hangover.
- **Fracture grows** from 20 to 30, because the questions it is built from already add up to more than 20.
- **Steady Climb and Hangover shrink.** Some of what they held is now counted as a US crisis or a fracture, and a bust inside a fractured world now counts as Fracture.
- **Worlds can rise and fall.** Names are attached to cells and groups, not fixed in advance. If a cell outside the named ones passes about 10%, it gets a name.

## How the weekly update would score it

1. Update each driver's own odds from its questions, signals and anchors, using the current evidence rule and 5-point cap.
2. Re-check the three links. Change a link only when evidence bears on the link itself, not just on one driver.
3. Recompute the twelve cells and the named worlds from those numbers, so the cells always agree with the drivers.
4. Record all of it in the weekly history, so old weeks can be compared cell by cell.

The cost: three driver estimates and three links take more judgment each week than four world odds, and few markets price joint outcomes directly. The gain is that each number on the site traces back to a driver someone can argue with.

## Open questions

- Does world order count a regional Gulf war as a fracture, or only great-power wars? The Gulf is the single biggest input to the 30%.
- Should "pays off" need transformative capability, or is a sustained, revenue-funded build-out enough? This draft accepts either.
- How to map the old weekly history: the four old worlds map onto the new ones only roughly, so the history chart may need a break at the switch.
