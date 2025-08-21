import pytest
from main import multiply

def test_multiply():
    assert 4 == multiply(9,10)