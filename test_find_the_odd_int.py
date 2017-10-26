"""Test to find the odd int."""
import pytest

TEST = [([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5),
        ([1, 1, 1, 1, 3], 3),
        ([1, 2, 3, 2, 3], 1),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 62], 62),
        ([1, 1, 2, 2, 3], 3)]


@pytest.mark.parametrize('para, result', TEST)
def test_find_the_odd_int(para, result):
    from find_the_odd_int import find_it
    assert find_it(para) == result
