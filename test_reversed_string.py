"""Test  revesded string"""
import pytest

TEST = [('world', 'dlrow'),
        ('hello', 'olleh'),
        ('', ''),
        ('h', 'h')]


@pytest.mark.parametrize("input,output", TEST)
def test_reversed_string(input, output):
    """test if string  reversed"""
    from reversed_string import solution
    assert solution(input) == output
