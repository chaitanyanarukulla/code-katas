""" Test for Multiples of 3 and 5 and then Returns the Sum of Multiples of 3 and 5"""
import pytest

TEST = [
    (10, 23),
    (15, 45),
    (25, 143),
    (100, 2318),
    (2, 0)
]

@pytest.mark.parametrize('input, output', TEST)
def test_sum_of_multy_3_and_5(input, output):
    """ Test Multiples of 3 and 5 - Return the Sum of Multiples of 3 and 5"""
    from sum_of_multy_3_and_5 import solution
    assert solution(input) == output