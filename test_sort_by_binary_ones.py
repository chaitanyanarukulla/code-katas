"""Testing for sort by binary"""
import pytest

TEST = [([1, 3], [3, 1]),
        ([1, 2, 3, 4], [3, 1, 2, 4]),
        ([1, 15, 7, 3, 5], [15, 7, 3, 5, 1]),
        ([2, 2048, 3], [3, 2, 2048]),
        ([5, 2049, 3], [3, 5, 2049])]


@pytest.mark.parametrize('input,output', TEST)
def test_sort_by_binary_ones(input, output):
    """test for sorting"""
    from sort_by_binary_ones import sort_by_binary_ones
    assert sort_by_binary_ones(input) == output
