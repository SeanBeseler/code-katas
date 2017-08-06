"""Testing the flight_path."""
import pytest
from flight_paths import get_path
data = [
    {'city': 'c1', 'destination_cities': ['c2', 'c3'], 'lat_lon': [0, 0]},
    {'city': 'c2', 'destination_cities': ['c1'], 'lat_lon': [0, 0]},
    {'city': 'c3', 'destination_cities': ['c4', 'c2'], 'lat_lon': [0, 0]}
]


def test_flight_path(l1='c2', l2='c3', result=['c3', 'c1', 'c2']):
    """Test to see if a path is chosen chosen.
    """
    assert get_path(l1, l2, data) == result


def test_get_path_error():
    """Test for error if city is not real."""
    with pytest.raises(KeyError):
        get_path('c1', 'not_real', data)
