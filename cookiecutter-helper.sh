#!/bin/bash

# CookieCutter Helper Script
# Edit the values below and run this script to generate a project

set -e

# Template path (current directory)
TEMPLATE_PATH="."

# Edit these values for your test
AUTHOR="Switchbox"
EMAIL="hello@switch.box"
AUTHOR_GITHUB_HANDLE="switchbox-data"
PROJECT_NAME="no-notebooks-test"
PROJECT_DESCRIPTION="This is a template repository for Python projects that use uv for their dependency management."
LANGUAGES="both"
INCLUDE_GITHUB_ACTIONS="n"
PUBLISH_TO_PYPI="y"
DEPTRY="n"
MKDOCS="n"
DEVCONTAINER="y"
TYPE_CHECKER="ty"
OPEN_SOURCE_LICENSE="MIT license"
AWS="y"
QUARTO="y"
JUPYTER="y"
PYDATA="n"
ISSUE_TEMPLATE="y"

# Generate project slug from project name
PROJECT_SLUG=$(echo "$PROJECT_NAME" | tr '[:upper:]' '[:lower:]' | sed 's/-/_/g')

# Create tmp directory if it doesn't exist
mkdir -p tmp

# Run cookiecutter with uvx in tmp directory
uvx cookiecutter "$TEMPLATE_PATH" \
    --output-dir tmp \
    --no-input \
    author="$AUTHOR" \
    email="$EMAIL" \
    author_github_handle="$AUTHOR_GITHUB_HANDLE" \
    project_name="$PROJECT_NAME" \
    project_slug="$PROJECT_SLUG" \
    project_description="$PROJECT_DESCRIPTION" \
    languages="$LANGUAGES" \
    include_github_actions="$INCLUDE_GITHUB_ACTIONS" \
    publish_to_pypi="$PUBLISH_TO_PYPI" \
    deptry="$DEPTRY" \
    mkdocs="$MKDOCS" \
    devcontainer="$DEVCONTAINER" \
    type_checker="$TYPE_CHECKER" \
    open_source_license="$OPEN_SOURCE_LICENSE" \
    aws="$AWS" \
    quarto="$QUARTO" \
    jupyter="$JUPYTER" \
    pydata="$PYDATA" \
    issue_template="$ISSUE_TEMPLATE"

echo "Project generated in tmp/$PROJECT_NAME"
