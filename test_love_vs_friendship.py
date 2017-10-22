import pytest

TEST = [('attitude', 100),
        ('friends', 75),
        ('family', 66),
        ('abc', 6)]
        
@pytest.mark.parametrize('input, output',TEST)
def test_words_to_marks(input,output):
    """test to find  sum totol of letters"""
    from love_vs_friendship import words_to_marks
    assert words_to_marks(input) == output
