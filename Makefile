install:
	uv sync
	
run:
	uv run gendiff --help

build:
	uv build

package-install:
	uv tool install dist/*.whl

overwriting:
	uv tool install dist/*.whl --force

uninstall hexlet-code:
	uv tool uninstall hexlet-code

lint:
	uv run ruff check gendiff

fix:
	uv run ruff check --fix gendiff
	uv run ruff check --fix tests

test-coverage:
	uv run pytest --cov=gendiff tests --cov-report xml

check:
	uv run pytest

hhh:
	uv tool uninstall hexlet-code
	uv build
	uv tool install dist/*.whl