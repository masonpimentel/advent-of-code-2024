## Advent of Code 2024

Python solutions for Advent of Code 2024 with code quality managed by these tools:

* Linting: pylint https://pylint.readthedocs.io/en/stable/
* Typing: mypy https://mypy-lang.org/
* Formatting: black https://black.readthedocs.io/en/stable/

Join my leaderboard! https://adventofcode.com/2024/leaderboard/private: `4780152-1e037a8f`

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
| Day 1 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | 
| Day 2 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | 
| Day 3 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | 
| Day 4 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | 
| Day 5 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | 
| Day 6 | 🟠 | ~ 5 | ~ 50 | ~ 53 | ~ 49 | This uses Python concurrent.futures.ProcessPoolExecutor - optimized for 16+ cores |
| Day 7 | 🟡 | ~ 2 | ~ 6 | ~ 5 | ~ 6 | This uses Python concurrent.futures.ProcessPoolExecutor - optimized for 16+ cores |
| Day 8 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 |
| Day 9 | 🟡 | ~ 2 | ~ 3 | ~ 3 | ~ 2 |
| Day 10 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 |
| Day 11 | 🔵 | < 0.1 | ~ 1 | ~ 1 | ~ 1 |
| Day 12 | 🔵 | < 0.1 | ~ 1 | < 0.1 | < 0.1 |
| Day 13 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 |
| Day 14 | 🟡 | ~ 4 | ~ 9 | ~ 7 | ~ 6 | |
| Day 15 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 16 | 🔵 | ~ 1 | ~ 1 | ~ 1 | ~ 1 | |
| Day 17 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 18 | 🟠 | ~ 8 | ~ 16 | ~ 12 | ~ 12 | This uses Python concurrent.futures.ProcessPoolExecutor, needs at least 2 cores |
| Day 19 | 🔵 | < 0.1 | ~ 1 | < 0.1 | < 0.1 | |
| Day 20 | 🟡 | ~ 3 | ~ 5 | ~ 4 | ~ 4 | |
| Day 21 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 22 | 🟠 | ~ 5 | ~ 12 | ~ 9 | ~ 8 | |
| Day 23 | 🔵 | ~ 1 | ~ 1 | ~ 1 | ~ 1 | |
| Day 24 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |
| Day 25 | 🟢 | < 0.1 | < 0.1 | < 0.1 | < 0.1 | |

### Install packages

Only dev packages are needed so use `--dev`

`pipenv install --dev`

### Running

Run using `pytest`

#### Mac

Use `./run-all.sh`

#### Windows

Use `.\run-all.ps1`

### Formatting

CI will check that all files are formatted according to `black`

To ensure CI will pass, run `pipenv run black --check .`

### MyPy

`pipenv run mypy src`

### Pylint

`pipenv run pylint src`

### Coverage

`pipenv run coverage run -m pytest`
`pipenv run coverage report`
