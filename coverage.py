[tox]
envlist = py39
skipsdist = True

[testenv]
deps = [
    pytest,
    pytest-cov ]
commands = [
    pytest --cov=src --cov-report=xml --cov-report=html ]

[coverage:run]
relative_files = True
source = src/
branch = True
