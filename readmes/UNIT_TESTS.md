# Pytest — Project Testing

[pytest](https://docs.pytest.org/) is a framework for writing and running
unit tests. `pytest-cov` (plugin) additionally calculates test coverage.

## Usage

```bash
uv run pytest                      # just run the tests (you can add -v to the end of the line for detailed output)
uv run pytest --cov=project -v     # tests + coverage percentage for project/ with details
uv run pytest --cov=project --cov-report=xml  # same + save report to a file
```

## Tests directory

All tests are in the `tests/` folder, mirroring the structure of `project/`:
- `tests/test_addition.py` — tests for `project/addition.py`
- `tests/test_template_paths.py` — tests for `project/helpers/template_paths.py`

## How to write a new test

  * The file must be named `test_*.py`, the function inside — `test_*`
   (otherwise pytest won't discover or run it)
  * Minimal example:

```python
from project.example import addition

def test_addition():
    assert addition(2, 3) == 5
```

## CI

Tests and coverage run automatically in GitHub Actions on every push —
see `.github/workflows/testing_and_coverage.yml`.