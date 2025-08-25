.PHONY: install virtualenv ipython test watch pflake8

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@.venv/bin/ipython

lint:
	@.venv/bin/pflake8

test:
	@.venv/bin/pytest -vv -s

watch:
	#@.venv/bin/ptw -- -vv -s
	@ls **/*.py | entr pytest
