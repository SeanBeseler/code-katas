"""Testing string pyrmid"""
import pytest
from pyrmid import count_all_characters_of_the_pyramid
from pyrmid import count_visible_characters_of_the_pyramid
from pyrmid import watch_pyramid_from_above
from pyrmid import watch_pyramid_from_the_side


def test_watch_side():
    """test with abc"""
    assert watch_pyramid_from_the_side('abc') == '  c  \n bbb \naaaaa'


def test_watch_side_empty():
    """test to make sure empty input works."""
    assert watch_pyramid_from_the_side('') == ''


def test_watch_side_none():
    """test to make sure no input works."""
    assert watch_pyramid_from_the_side() is None


def test_watch_top():
    """test with abc"""
    assert watch_pyramid_from_above('abc') == 'aaaaa\nabbba\nabcba\nabbba\naaaaa'


def test_watch_top_empty():
    """test to make sure empty input works."""
    assert watch_pyramid_from_above('') == ''


def test_watch_top_none():
    """test to make sure no input works."""
    assert watch_pyramid_from_above() is None


def test_count_visable():
    """test with abc"""
    assert count_visible_characters_of_the_pyramid('abc') == 25


def test_count_visable_none():
    """test to make sure no input works."""
    assert count_visible_characters_of_the_pyramid() == -1
