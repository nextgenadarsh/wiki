pipenv
---

## Features 


- You no longer need to use pip and virtualenv separately: they work together.
- Pipenv uses `Pipfile` and `Pipfile.lock` to separate abstract dependency declarations from the last tested combination.
- Hashes are documented in the lock file which are verified during install.
- Gives you insight into your dependency graph (e.g. $ pipenv graph).
- Supports local customizations with .env files

- Enables truly deterministic builds, while easily specifying only what you want.
- Generates and checks file hashes for locked dependencies.
- Automatically install required Pythons, if pyenv or asdf is available.
- Automatically finds your project home, recursively, by looking for a Pipfile.
- Automatically generates a Pipfile, if one doesn't exist.
- Automatically creates a virtualenv in a standard location.
- Automatically adds/removes packages to a Pipfile when they are installed/uninstalled.
- Automatically loads .env files, if they exist.

## Basic Concepts


- A virtualenv will automatically be created, when one doesn't exist.
- When no parameters are passed to install, all packages [packages] specified will be installed. Otherwise, whatever virtualenv defaults to will be the default.

## Getting started

- Install pipenv `pip install --user pipenv`
- Create a new project using Python 3.7, specifically: `pipenv --python 3.7`
- Remove project virtualenv (inferred from current directory): `pipenv --rm`
- Install all dependencies for a project (including dev): `pipenv install --dev`
- Create a lockfile containing pre-releases: `pipenv lock --pre`
- Show a graph of your installed dependencies: `pipenv graph`
- Check your installed dependencies for security vulnerabilities: `pipenv check`
- Install a local setup.py into your virtual environment/Pipfile: `pipenv install -e .`
- Use a lower-level pip command: `pipenv run pip freeze`

- Create new environment using python 3.6: `pipenv install --python 3.6`
- Locate the project: `pipenv --where`
- Locate the virtualenv: `pipenv --venv`
- Locate python interpreter: `pipenv --py`
- Activate virtualenv: `pipenv shell`
- Install packages: `pipenv install`


> References

- [pipenv](https://pypi.org/project/pipenv/#pipenv-python-development-workflow-for-humans)
