[![linting workflow](https://github.com/sshvets0v/python-project-template/actions/workflows/linting.yml/badge.svg)](https://github.com/sshvets0v/python-project-template/actions/workflows/linting.yml)
[![testing and coverage workflow](https://github.com/sshvets0v/python-project-template/actions/workflows/testing_and_coverage.yml/badge.svg)](https://github.com/sshvets0v/python-project-template/actions/workflows/testing_and_coverage.yml)
[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.githubusercontent.com/sshvets0v/e8ec108de82c4a3c759a6ba2d114c028/raw/clone.json&logo=github)](https://github.com/MShawon/github-clone-count-badge)


# python-project-template
Template for UNN python projects
## Structure
  * **Pyproject.toml** - a configuration file that stores project metadata, dependencies and tool settings in TOML format. 
  * **uv.lock** - a file that locks in specific project settings, thereby ensuring consistent project behavior for everyone who has installed it.
  * **"project"** - a directory (package) that stores project's modules.
  * **"project/data"** - a directory containing data files used by the code.
  * **"notebooks"** - a directory that stores .ipynb files related to your project (e.g. drafts, experiments with data, data visualization). These files are not subject to testing.
  * **"imgs"** - a directory that stores image files related to your project.
  * **"readmes"** - a directory intended for storing various README.md files (e.g. README for a specific library or other technology).
  * **"tests"** - a directory containing unit tests for your project's modules.
  * **.github/workflows/** — CI pipeline: linting, testing and coverage, run automatically on every push (currently on 'main' branch, could be changed).
## Installation
  * Before installing this project, uv must be installed. Follow the link below to the developer's official website for installation instructions: https://docs.astral.sh/uv/getting-started/installation/
  * Project installation and synchronizing local device settings with the settings pinned in the uv.lock file
```
git clone https://github.com/mike-live/python-project-template.git 
cd python-project-template
uv sync
```
## Usage
```python
from project.addition import addition
from project.helpers import PROJECT_DATA_DIR

addition(2, 3)
```
## Development
```bash
`uv run ruff check .` - read more [readmes/LINTER.md](readmes/LINTER.md)
`uv run pytest --cov=project` - read more [readmes/UNIT_TESTS.md](readmes/UNIT_TESTS.md)
```