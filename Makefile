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


