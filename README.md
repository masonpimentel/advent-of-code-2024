## Advent of Code 2024

The purpose of this project is to provide Python solutions for Advent of Code 2024.

https://adventofcode.com/2024

Join my leaderboard! https://adventofcode.com/2024/leaderboard/private: `4780152-1e037a8f`

## TODO

* Refactor, clean code, improve code quality
* Improve performance

### Install packages

`pipenv run sync`

### Running

#### Mac

`PYTHONPATH="src" pipenv run pytest -s test`

#### Windows

`$env:PYTHONPATH="src"; pipenv run pytest -s test`

### Formatting

CI will check that all files are formatted according to `black`

To ensure CI will pass, run `pipenv run black --check .`

