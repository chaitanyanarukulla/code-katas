""" TESTING Highest and Lowest From a String"""
import pytest

TEST = [("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6", "542 -214"),
        ("1 -1", "1 -1"),
        ("1 1", "1 1"),
        ("42 42", "42 42"),
        ("-1 -1 0", "0 -1"),
        ]


@pytest.mark.parametrize('input,output', TEST)
def test_high_and_low(input, output):
    """test the  inputs and outputs"""
    from highest_and_lowest import high_and_low
    assert high_and_low(input) == output
