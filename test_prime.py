"""Tests for prime.py."""

import pytest


TEST_CHECK_MAT_OUTPUT = [
([[ 1,   3, -4,   5, -2,  5,  1],
  [  2,   0, -7,   6,  8,  8, 15],
  [  4,   4, -2, -10,  7, -1,  7],
  [ -1,   3,  1,   0, 11,  4, 21],
  [ -7,   6, -4,  10,  5,  7,  6],
  [ -5,   4,  3,  -5,  7,  8, 17],
  [-11,   3,  4,  -8,  6, 16,  4]] , [3,8])
]



@pytest.mark.parametrize('matr, result', TEST_CHECK_MAT_OUTPUT)
def test_check_prime(number, result):
    """Check sum of matrix"""
    from Matrix import avg_diags
    assert avg_diags(matr) == result


