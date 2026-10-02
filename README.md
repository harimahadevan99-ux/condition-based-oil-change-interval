# OilPlanner - condition-based oil change interval

**Idea 10/10 - category: Maintenance**

## Problem
Fixed oil change intervals (e.g. 500 h) over-service lightly loaded machines and under-protect severely loaded ones. Both cost money.

## What this prototype does
Combines oil analysis parameters (viscosity change, iron, soot, TBN loss) into a condition index, forecasts hours until the limit and recommends a change point with a safety margin.

## KPIs
- Recommended interval (h)
- Change events avoided per year
- Oil litres saved

## Quick start
```bash
python src/demo.py                      # run the demo on synthetic data
python -m unittest discover -s tests -v # run the tests
jupyter notebook notebooks/             # optional: interactive demo
```
Core code is pure Python 3.9+ without dependencies (see `requirements.txt` for optional extras).

## Data
Replace simulate.py with oil sample lab data or inline oil sensor readings.
All numbers in `src/simulate.py` and `data/sample_data.json` are synthetic and only for demonstration; calibrate against real machine data before drawing conclusions.

## Roadmap
- [ ] Machine-specific limits from OEM
- [ ] Duty-cycle based prior (severe vs light)
- [ ] Filter differential pressure input
- [ ] Auto-schedule in service planning tool

## Repository structure
| Path | Purpose |
|---|---|
| `src/core.py` | Algorithm / business logic |
| `src/simulate.py` | Synthetic data generator |
| `src/demo.py` | Runnable example |
| `tests/` | Unit tests |
| `data/` | Sample data (put real exports in `data/raw/`) |
| `models_artifacts/` | Trained models and calibration files (empty for now) |
| `notebooks/` | Jupyter demo notebook |
| `.github/workflows/ci.yml` | GitHub Actions: tests + demo on every push |
| `requirements.txt` | Optional dependencies |
| `LICENSE` | MIT |

## Extend with AI
Open the repo in GitHub Codespaces or Claude Code / Copilot and try prompts such as:
- "Read src/core.py and add a CSV loader for telematics exports with column mapping."
- "Add a Streamlit dashboard that visualises the demo output."
- "Write more unit tests for edge cases and sensor dropouts."

## Licence
MIT
