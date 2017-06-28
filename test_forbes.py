"""Test the forbes code."""
from forbes import get_billionaire

def test_forbes():
    """Test to see if works with the data."""
    assert get_billionaire('data.json') == (['Phil Knight', 24400000000, 'Nike', 'Mark Zuckerberg', 44600000000, 'Facebook'])


def test_edge_cases():
    """Test ot see if works with mod data."""
    assert get_billionaire('editedData.json') == (['Carlos Slim Helu', 50000000000, 'telecom','Sergey Brin', 34400000000, 'Google'])
