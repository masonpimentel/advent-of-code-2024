## Advent of Code 2024

![Build Status](https://github.com/masonpimentel/advent-of-code-2024/actions/workflows/ci.yml/badge.svg) [![codecov](https://codecov.io/gh/masonpimentel/advent-of-code-2024/branch/master/graph/badge.svg)](https://codecov.io/gh/masonpimentel/advent-of-code-2024/)

Python solutions for Advent of Code 2024 (https://adventofcode.com/2024/) with code quality managed by these tools:

* Linting: pylint https://pylint.readthedocs.io/en/stable/
* Typing: mypy https://mypy-lang.org/
* Formatting: black https://black.readthedocs.io/en/stable/

Join my leaderboard! https://adventofcode.com/2024/leaderboard/private: `4780152-1e037a8f` (note you need to be signed in to join private leaderboards)

### Performance

Machines:

| Name | Description   | os.cpu_count() |
| --- | --- | --- |
| PC (local) | Intel Core i5 12600K (local machine)   | 16 |
| Mac (local) | Intel Core i5 8210Y (local machine) | 4 |
| Gitlab runner | saas-linux-small-amd64   | 2 |
| Github runner | ubuntu-24.04  | 2 |

Runtime (seconds):

| Day | Status | PC | Mac | Gitlab runner | Github runner | Notes |
| ----- | --- | --- | --- | --- | --- | --- |
| Day 1 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 2 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 3 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 4 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 5 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 6 | 🟠 | ~ 5 | ~ 59 | ~ 56 | ~ 53 | This uses Python concurrent.futures.ProcessPoolExecutor - optimized for 16+ cores |
| Day 7 | 🟡 | ~ 2 | ~ 14 | ~ 12 | ~ 12 | This uses Python concurrent.futures.ProcessPoolExecutor - optimized for 16+ cores |
| Day 8 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 9 | 🟡 | ~ 2 | ~ 3 | ~ 3 | ~ 2 | |
| Day 10 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 11 | 🔵 | < 0.1 | ~ 1 | ~ 1 | ~ 1 | |
| Day 12 | 🔵 | < 0.1 | ~ 1 | ~ 1 | ~ 1 | |
| Day 13 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 14 | 🟡 | ~ 4 | ~ 9 | ~ 7 | ~ 6 | |
| Day 15 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 16 | 🔵 | ~ 1 | ~ 1 | ~ 1 | ~ 1 | |
| Day 17 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 18 | 🟠 | ~ 8 | ~ 17 | ~ 12 | ~ 12 | This uses Python concurrent.futures.ProcessPoolExecutor, needs at least 2 cores |
| Day 19 | 🔵 | < 0.1 | ~ 1 | < 0.1 | < 0.1 | |
| Day 20 | 🟡 | ~ 3 | ~ 5 | ~ 4 | ~ 4 | |
| Day 21 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 22 | 🟡 | ~ 5 | ~ 12 | ~ 9 | ~ 8 | |
| Day 23 | 🔵 | ~ 1 | ~ 1 | ~ 1 | ~ 1 | |
| Day 24 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 25 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |

### Install packages

Only dev packages are needed so use `--dev`

`pipenv install --dev`

### Running

Run using `pytest` and see solution output

#### Mac

Use `./run.sh`

#### Windows

Use `.\run.ps1`

### Formatting

CI will check that all files are formatted according to `black`

To ensure CI will pass, run `pipenv run black --check .`

### MyPy

`pipenv run mypy src`

### Pylint

`pipenv run pylint src`

### To run all the above

Use `./run-all.sh` or `.\run-all.ps1`

### To get average time over n runs

`pipenv run pytest -s test --runs n`

Example for the average over 3 runs: `pipenv run pytest -s test --runs 3`
