### Hexlet tests and linter status:
[![Actions Status](https://github.com/ivanvasutinskiy/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ivanvasutinskiy/python-project-50/actions)

[![Python CI](https://github.com/ivanvasutinskiy/python-project-50/actions/workflows/main.yaml/badge.svg)](https://github.com/ivanvasutinskiy/python-project-50/actions/workflows/main.yaml)

[![Maintainability](https://api.codeclimate.com/v1/badges/773d277682748a9d4c75/maintainability)](https://codeclimate.com/github/ivanvasutinskiy/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/773d277682748a9d4c75/test_coverage)](https://codeclimate.com/github/ivanvasutinskiy/python-project-50/test_coverage)

# Вычислитель отличий (Python)

Второй проект на [Hexlet](https://ru.hexlet.io/programs/python/projects/50): Вычислитель отличий.   Программа: Python-разработчик.

Проект направлен на работу с коллекциями. Gendiff — это утилита командной строки для сравнения двух конфигурационных файлов. Инструмент анализирует файлы и отображает различия в удобочитаемом формате. Он поддерживает форматы файлов JSON и YAML.

## Установка

Клонируем GitHub репозиторий
```
$ git clone https://github.com/ivanvasutinskiy/python-project-50.git
```
Устанавливаем UV
```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Запуск программы

```
$ uv sync
$ uv build 
$ uv tool install dist/*.whl
```

## Описание

### Вывод справки

```
$ uv run gendiff --help
```

- -h, --help — отобразить это справочное сообщение и выйти.
- f FORMAT, --format FORMAT — задайте формат вывода (plain / json / stylish)

## Примеры работы программы:

### STYLISH формат

```
$ uv run gendiff ./tests/fixtures/file1.json ./tests/fixtures/file2.json
```

[![asciicast](https://asciinema.org/a/exuViPa6aApWM7j2JkUgqvsLz.svg)](https://asciinema.org/a/exuViPa6aApWM7j2JkUgqvsLz)

### PLAIN формат

```
$ uv run gendiff -f plain ./tests/fixtures/file1.json ./tests/fixtures/file2.json
```

[![asciicast](https://asciinema.org/a/W1XDfIOWOAC6BaczmTWDxXDUK.svg)](https://asciinema.org/a/W1XDfIOWOAC6BaczmTWDxXDUK)

### JSON формат

```
$ uv run gendiff -f json ./tests/fixtures/file1.json ./tests/fixtures/file2.json
```

[![asciicast](https://asciinema.org/a/BKzz3iVXjXAQKjkRCAFYqW3Kr.svg)](https://asciinema.org/a/BKzz3iVXjXAQKjkRCAFYqW3Kr)











