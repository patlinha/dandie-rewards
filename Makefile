.PHONY: install virtualenv ipython test watch

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -vv -s

watch:
	#@.venv/bin/ptw -- -vv -s
	@ls **/*.py | entr pytest
