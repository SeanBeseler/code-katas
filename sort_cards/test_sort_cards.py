import pytest
from sort_cards import sort_cards


def test_sort():
    """test the sort"""
    assert sort_cards(['K', 'A', 'Q']) == ['A', 'Q', 'K']


def test_sort_None():
    assert sort_cards() is None


def test_sort_empty():
    assert sort_cards('') == ''
