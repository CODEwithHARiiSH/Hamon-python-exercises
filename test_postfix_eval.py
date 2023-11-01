from evaluation import *

def test_single_operator():
    assert evaluat("2") == 2
    
def test_with_addition():
    assert evaluat("2+4") == 6
