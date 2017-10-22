"""TEST to  test Remove n exclamation marks in the sentence from left to right"""
import pytest
TEST = [
    [["Hi!",1] , "Hi"],
    [["Hi!",100] , "Hi"],
    [["Hi!!!",1] , "Hi!!"],
    [["Hi!!!",100] , "Hi"],
    [["!Hi",1] , "Hi"],
    [["!Hi!",1] , "Hi!"],
    [["!Hi!",100] , "Hi"],
    [["!!!Hi !!hi!!! !hi",1] , "!!Hi !!hi!!! !hi"],
    [["!!!Hi !!hi!!! !hi",3] , "Hi !!hi!!! !hi"],
    [["!!!Hi !!hi!!! !hi",5] , "Hi hi!!! !hi"],
    [["!!!Hi !!hi!!! !hi",100] , "Hi hi hi"],
]

@pytest.mark.parametrize('parm1,parm2','output',TEST)
    """ test to remove Exclamation marks"""
def test_remove_excl(parm1,parm2,output):
    from remove_excl import remove
    assert remove(parm1,parm2) == output