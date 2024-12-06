# -*- coding: utf-8 -*-
import re

# validation on user input
INPUT_VALIDATION = [
    ("project", "{{ cookiecutter.project }}", r"^[a-zA-Z][a-zA-Z0-9 _-]+$"),
    ("package", "{{ cookiecutter.package }}", r"^[a-z][a-z0-9_]+$"),
]


def _check_input(name: str, value: str, regex: str) -> None:
    if not re.match(regex, value):
        raise ValueError(f"'{name}' should match {regex=}, got: {name}='{value}'")


_ = [_check_input(*validation) for validation in INPUT_VALIDATION]

# update cookiecutter context
"""
{{ cookiecutter.update({"linelength": 120 }) }}
"""
