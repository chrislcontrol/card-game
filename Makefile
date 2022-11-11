.DEFAULT_GOAL := default_target
.PHONY: default_target test clean setup create-venv setup-dev setup-os git-up code-convention test run all

PIP := pip install
PROJECT_NAME := card-game
PYTHON_VERSION := 3.10.4
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

# Environment setup
.pip:
	pip install --upgrade pip

setup-dev: .pip
	$(PIP) -e .[dev]

setup-production: .pip
	$(PIP) -e

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev

code-convention:
	flake8
	pycodestyle
