"""Test Template."""

import pytest

from src.package import hello


@pytest.mark.unit
def test_hello():
    """Validate package is importable"""
    assert hello.hello_world() == "Hello World!"
