from __future__ import annotations

import importlib.metadata

import yourbuddy as m


def test_version():
    assert importlib.metadata.version("yourbuddy") == m.__version__
