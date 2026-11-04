# Futures Watch 2030

An open scenario forecast for the years to the end of 2029. It gives odds on four ways the period could go (Steady Climb, Takeoff, Hangover and Fracture), reads the same evidence as seven sci-fi futures, and tracks the big what-ifs, signals and milestones behind them. Everything is re-scored every week against prediction markets, expert forecasts and live data.

The site rebuilds from the files in this repo. The odds are refreshed every Monday, and each weekly update arrives as a pull request, so you can see every number that moved and why.

> A tool for thinking about the future, not financial, legal or career advice.

## What's in here

```
worlds/        the four worlds, one file each, odds sum to 100
scifi/         the seven sci-fi futures, odds sum to 100
questions/     the big what-ifs: outcomes, forecaster anchors, linked signals
signals/       indicators re-checked weekly: latest reading, thresholds, source
readings/      one CSV per signal: every weekly reading, for the history charts
milestones/    single events before 2030 and their odds
checks/        short-range forecasts that resolve within months and get scored
tracker/       meta (headline, this week, scorecard), calendar, update log, history
scripts/       validate.py and build.py
site/          the web page that renders data.json
METHODOLOGY.md how worlds are classified, how odds move, how checks are scored
CONTRIBUTING.md how to add a signal, a forecast or a what-if
```

## Suggest a factor

The most useful thing you can add is a **factor we should be watching**: a data series, market, benchmark or published forecast that would tell us which world we're heading into.

1. Copy `signals/_template.yaml` to `signals/<your-id>.yaml` and fill it in. Leave `tracking: proposed`.
2. Run `python scripts/validate.py`.
3. Open a pull request.

The weekly review checks the source, adds a first reading and links the signal to the what-ifs it informs. You can also [open an issue](../../issues/new?template=suggest-a-factor.yml) if you'd rather not edit files. Full guide: [CONTRIBUTING.md](CONTRIBUTING.md).

## Run it locally

```sh
pip install pyyaml
python scripts/validate.py
python scripts/build.py
python -m http.server -d _site 8000   # open http://localhost:8000
```

## License

Code is MIT. Data and text in `worlds/`, `scifi/`, `questions/`, `signals/`, `readings/`, `milestones/`, `checks/` and `tracker/` are CC BY 4.0. See [LICENSE.md](LICENSE.md).
