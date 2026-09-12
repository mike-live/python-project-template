# Ruff — project linter

[Ruff](https://docs.astral.sh/ruff/) — a fast linter and formatter for Python,
written in Rust. It replaces the combination of flake8, isort, pyupgrade, and black.

## Usage

```bash
uv run ruff check .          # checks code
uv run ruff check . --fix    # checks and automatically fixes what it can fix
uv run ruff format .         # formats code
```

## Selected rules

The settings are in `pyproject.toml`, section `[tool.ruff.lint]`.

| Rule code | What it does|
|-----|----------------|
| E, W | pycodestyle — basic code style (indentation, whitespace, line length) |
| F   | pyflakes — checks for unused imports/variables, undefined names |
| UP  | pyupgrade — checks for outdated Python syntax that can be modernized |
| S   | flake8-bandit (security) |

A complete list of all available rules: https://docs.astral.sh/ruff/rules/

## Changing rules of linter
To add or remove rules, you need to add or remove the corresponding rule codes in the `tools.ruff.lint` section.
To specify a list of rules instead of the defaults, use `select`.
```bash
[tool.ruff.lint]
select = [
    ...
]
```
To add rules to the default set, use `extend-select`.
```bash
[tool.ruff.lint]
extend-select = [
    ...
]
```

## Disabling a rule

- **`# noqa: CODE`** — disables a rule on one specific line. Use this
  most often, for one-off exceptions.
```python
  import os  # noqa: W
```
- **`ignore`** in `[tool.ruff.lint]` — disables a rule throughout the entire project.
  Use carefully because this affects every file, including future ones.
```toml
  [tool.ruff.lint]
  ignore = ["F"]
```
- **`exclude`** in `[tool.ruff]` — skips entire files/folders, ruff
  doesn't check them.
```toml
  [tool.ruff]
  exclude = ["notebooks"]
```
- **`per-file-ignores`** in `pyproject.toml` — disables a rule for an
  entire file.
```toml
  [tool.ruff.lint.per-file-ignores]
  "project/helpers/template_paths.py" = ["F"]
```

## CI

Linting runs automatically in GitHub Actions on every push —
see `.github/workflows/linting.yml`.