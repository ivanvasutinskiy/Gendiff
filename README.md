### Hexlet tests and linter status:
[![Actions Status](https://github.com/ivanvasutinskiy/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ivanvasutinskiy/python-project-50/actions)

[![Python CI](https://github.com/ivanvasutinskiy/python-project-50/actions/workflows/main.yaml/badge.svg)](https://github.com/ivanvasutinskiy/python-project-50/actions/workflows/main.yaml)

[![Maintainability](https://api.codeclimate.com/v1/badges/773d277682748a9d4c75/maintainability)](https://codeclimate.com/github/ivanvasutinskiy/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/773d277682748a9d4c75/test_coverage)](https://codeclimate.com/github/ivanvasutinskiy/python-project-50/test_coverage)

# Gendiff (Python)

The second project on [Hexlet](https://ru.hexlet.io/programs/python/projects/50): Gendiff.   Program: Python developer.

The project is aimed at working with collections. Gendiff is a command—line utility for comparing two configuration files. The tool analyzes the files and displays the differences in a readable format. It supports JSON and YAML file formats.

## Installation

Cloning the GitHub repository
```
$ git clone https://github.com/ivanvasutinskiy/python-project-50.git
```
UV Installation
```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Launching the program

```
$ uv sync
$ uv build 
$ uv tool install dist/*.whl
```

## Description

### Help output

```
$ uv run gendiff --help
```

- -h, --help — display a help message and exit.
- -f FORMAT, --format FORMAT — set the output format (plain / json / stylish)

## Examples of how the program works:

### STYLISH format (default)

```
$ uv run gendiff ./tests/fixtures/file1.json ./tests/fixtures/file2.json
```

[![asciicast](https://asciinema.org/a/exuViPa6aApWM7j2JkUgqvsLz.svg)](https://asciinema.org/a/exuViPa6aApWM7j2JkUgqvsLz)

### PLAIN format

```
$ uv run gendiff -f plain ./tests/fixtures/file1.json ./tests/fixtures/file2.json
```

[![asciicast](https://asciinema.org/a/W1XDfIOWOAC6BaczmTWDxXDUK.svg)](https://asciinema.org/a/W1XDfIOWOAC6BaczmTWDxXDUK)

### JSON format

```
$ uv run gendiff -f json ./tests/fixtures/file1.json ./tests/fixtures/file2.json
```

[![asciicast](https://asciinema.org/a/BKzz3iVXjXAQKjkRCAFYqW3Kr.svg)](https://asciinema.org/a/BKzz3iVXjXAQKjkRCAFYqW3Kr)











