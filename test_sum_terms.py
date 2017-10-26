"""Testing  the  function which returns the sum of following
series upto nth term(parameter)."""
import pytest

TEST = [(1, "1.00"),
        (4, "1.49"),
        (6, "1.63"),
        (15, "1.94"),
        (58, "2.40")]


@pytest.mark.parametrize('input,output', TEST)
def test_series_sum(input, output):
    """test for the sum of following nth series"""
    from sum_terms import series_sum
    assert series_sum(input) == output