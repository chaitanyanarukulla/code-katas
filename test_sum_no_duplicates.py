import  pytest

TEST = [([1, 1, 2, 3], 5),
        ([5, 6, 10, 3, 10, 10, 6, 7, 0, 9, 1, 1, 6, 3, 1], 21),
        ([0, 10, 8, 9, 7, 3, 3, 9, 3, 6, 0], 31),
        ([7, 10, 10, 9, 0, 2, 5, 10, 3, 8, 1, 4, 9, 9, 5, 8, 8, 8, 5, 3], 14),
        ([1, 4, 3, 8, 9, 4, 7, 5, 10, 10, 7, 6, 9, 3], 20),
        ([2, 0, 4, 2, 2, 3, 6, 7, 3, 8, 10, 6, 8], 21)
        ]


@pytest.mark.parametrize('input,output', TEST)
def test_sum_no_duplicates(input, output):
    from sum_no_duplicate import sum_no_duplicates
    assert sum_no_duplicates(input) == output
