#!/usr/bin/env python
from __future__ import annotations

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def move_file(filepath: str, target: str) -> None:
    os.rename(os.path.join(PROJECT_DIRECTORY, filepath), os.path.join(PROJECT_DIRECTORY, target))


def move_dir(src: str, target: str) -> None:
    shutil.move(os.path.join(PROJECT_DIRECTORY, src), os.path.join(PROJECT_DIRECTORY, target))


if __name__ == "__main__":
    # Handle language selection logic
    languages = "{{cookiecutter.languages}}"
    python_enabled = languages in ["python", "both"]
    r_enabled = languages in ["r", "both"]
    
    if not python_enabled:
        # Remove Python-specific files
        remove_file("pyproject.toml")
        remove_file("tox.ini")
        remove_dir("{{cookiecutter.project_slug}}")
        remove_dir("tests")
        # Remove Python-related GitHub Actions
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(".github/workflows/main.yml")
            remove_file(".github/workflows/on-release-main.yml")
    
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")
    else:
        if "{{cookiecutter.mkdocs}}" != "y" and "{{cookiecutter.publish_to_pypi}}" == "n":
            remove_file(".github/workflows/on-release-main.yml")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")

    # Handle notebooks directory based on quarto and jupyter selections
    quarto_enabled = "{{cookiecutter.quarto}}" == "y"
    jupyter_enabled = "{{cookiecutter.jupyter}}" == "y"
    pydata_enabled = "{{cookiecutter.pydata}}" == "y" and python_enabled

    if not quarto_enabled and not jupyter_enabled:
        # No notebooks at all
        remove_dir("notebooks")
    else:
        # Always remove R example (not supported yet)
        remove_file("notebooks/r_example.qmd")

        # Handle Quarto files
        if not quarto_enabled:
            # Remove all Quarto files
            remove_file("notebooks/_quarto.yml")
            remove_file("notebooks/index.qmd")
            remove_file("notebooks/md_example.qmd")
            remove_file("notebooks/py_example.qmd")
        else:
            # Keep Quarto files, but remove Python example if pydata not selected
            if not pydata_enabled:
                remove_file("notebooks/py_example.qmd")

        # Note: Justfile is kept regardless of quarto/jupyter selection
        # because it contains conditional sections for both

        # Handle Jupyter files
        if not jupyter_enabled:
            # Remove all Jupyter files
            remove_file("notebooks/md_example.ipynb")
            remove_file("notebooks/py_example.ipynb")
        else:
            # Keep Jupyter files, but remove Python example if pydata not selected
            if not pydata_enabled:
                remove_file("notebooks/py_example.ipynb")

    if "{{cookiecutter.open_source_license}}" == "MIT license":
        move_file("LICENSE_MIT", "LICENSE")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "BSD license":
        move_file("LICENSE_BSD", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "ISC license":
        move_file("LICENSE_ISC", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "Apache Software License 2.0":
        move_file("LICENSE_APACHE", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "GNU General Public License v3":
        move_file("LICENSE_GPL", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")

    if "{{cookiecutter.open_source_license}}" == "Not open source":
        remove_file("LICENSE_GPL")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")

    if "{{cookiecutter.issue_template}}" != "y":
        remove_dir(".github/ISSUE_TEMPLATE/")
