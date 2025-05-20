# Makefile

.PHONY: code-coverage server test unit-test integration-test black isort flake8 bandit

code-coverage:
	poetry run pytest --cov=src tests/

server:
	poetry run server

test:
	poetry run pytest tests/

unit-test:
	poetry run pytest -m "unit"

integration-test:
	poetry run pytest -m "integration"

black:
	poetry run black src/ tests/

isort:
	poetry run isort src/ tests/

flake8:
	poetry run flake8 src/ tests/

bandit:
	poetry run bandit -r src/ tests/ -c bandit.yaml