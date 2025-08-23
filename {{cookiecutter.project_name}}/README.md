# {{cookiecutter.project_name}}

[![Release](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/main.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
- **Documentation** <https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/>

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
git push -u origin main
```

### 2. Set Up Your Development Environment

If you installed devcontainers, simply open up this repo with VSCode and you'll be prompted to build and open the container.

If you prefer to work outside of a container, install the environment and the pre-commit hooks with

```bash
just install
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

### 5. Finishing setting up tools

{% if cookiecutter.mkdocs == "y" -%}
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/mkdocs/#enabling-the-documentation-on-github).
{%- endif %}

{% if cookiecutter.publish_to_pypi == "y" -%}
To finalize the set-up for publishing to PyPI, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi).
{%- endif %}

### 6. Clean up README

You are now ready to start development on your project!

Please delete **Getting started with you project** of this README.

## Developing

To simplify development, this project uses the [just](https://github.com/casey/just) command runner for all major tasks.

Available commands are defined in [Justfile](Justile). To view available them:

```bash
just
```

or
```bash
just --list
```

## Setting up development environment


{% if cookiecutter.devcontainer == "y" -%}
### With devcontainers
Given that many projects require system dependencies, the easiest way to define and distribute a reproducible development environment is with [devcontainers](https://containers.dev/). 

To load this project's devcontainer, open up the repo in VSCode (or a VSCode fork like Cursor or Positron.)

The editor will auto-detect the presence of the repo's devcontainer (configured in [.devcontainer/devcontainer.json](.devcontainer/devcontainer.json)). Click "Reopen in Container" to launch the devcontainer. uv will install python packages inside the container.{%- endif %}

### With uv

This package uses [uv](https://docs.astral.sh/uv/) for managing python versions, virtual environments, and packages.

First, install [just](https://github.com/casey/just).

Then, you can install uv, install the pre-commit hooks, launch the virtualenv, and download the packages (pinned in [uv.lock](uv.lock)) by running:

```bash
just install
```

## Adding a package
To add a python package to the project:

```bash
uv add <package-name>
```

This replaces `pip install <package-name>`, and has the effect of adding the package to [pyproject.toml](pyproject.toml), as well as pinning the package version in [uv.lock](uv.lock).

## Adding a development tool
To add a package that will only be used as a development tool:

```bash
uv add --dev <package-name>
```

This will update the dev `dependency-groups` in [pyproject.toml](pyproject.toml), and ensure that the package isn't declared as a run-time dependency of the library itself.

## Running code quality checks

We use [ruff](https://github.com/astral-sh/ruff) for linting and code formatting, {% if cookiecutter.type_checker == "mypy" -%}[mypy](https://mypy.readthedocs.io/en/stable/running_mypy.html){%- elif cookiecutter.type_checker == "ty" -%}[ty](https://docs.astral.sh/ty/){%- endif %} for type checking, and a series of [post-commit hooks](pre-commit-config.yaml) for validating YAML, JSON, whitespaces, and so on.

To run code quality checks:

```bash
just check
```

The checks will also be run automatically by Github Actions when opening PRs, merging to main, or creating a new release.

## Running tests

Our test are written using `pytest` and live in [tests/](tests/). They are checked against multiple python versions using `tox`.

To run the tests:

```bash
just test
```

{% if cookiecutter.mkdocs == "y" -%}
## Rendering docs

We use `mkdocs` and [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) for writing and rendering docs. The docs are written in markdown and live in [docs/](docs/).

To dynamically render the docs as you develop them:

```bash
just docs
```

To statically render the docs into HTML:

```bash
just docs-test
```

The docs are served by Github Pages out of the `gh-pages` branch. We do not publish them manually: they are automatically rendered and published by the Github Actions workflow when merging to `main`.
{%- endif %}

{% if cookiecutter.include_github_actions == "y" -%}
## Triggering the CI/CD pipeline

We use Github Actions to run tests, run code quality checks, and publish docs when you open a pull request, merge to main, or when you create a new release.
{%- endif %}

{% if cookiecutter.publish_to_pypi == "y" -%}
## Releasing a new version

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/settings/secrets/actions/new).
- Create a [new release](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/cicd/#how-to-trigger-a-release).
{%- endif %}

---

Repository initiated with [switchbox-data/cookiecutter-sb](https://github.com/fpgmaas/cookiecutter-uv), based off of [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
