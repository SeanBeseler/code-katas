import pytest
from proper_parenthetics import check_prens


def test_return_open():
    """test that prens are open"""
    assert check_prens('()()()(') == 1


def test_return_broken():
    """test that prens are broken"""
    assert check_prens('()()())()') == -1


def test_return_bal():
    """test that prens are balence"""
    assert check_prens('()()()()') == 0
