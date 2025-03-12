[tox]
envlist = py39
skipsdist = True

[testenv]
deps =
    pytest
    pytest-cov
commands =
    coverage run -m pytest
    coverage xml

[coverage:run]
relative_files = True
source = src/
branch = True
