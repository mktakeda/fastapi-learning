# Makefile

.PHONY: code-coverage server test unit-test black isort flake8 bandit

code-coverage:
	poetry run pytest --cov=src tests/

server:
	poetry run server

test:
	poetry run pytest tests/

unit-test:
	poetry run pytest -m "unit"

black:
	poetry run black src/ tests/

isort:
	poetry run isort src/ tests/

falke8:
	poetry run flake8 src/ tests/

bandit:
	poetry run bandit -r src/ tests/