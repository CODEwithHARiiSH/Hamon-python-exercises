from evaluation import *

def test_single_operator():
    assert evaluat("2") == 2
    
def test_operand_addition():
    assert evaluat("24+") == 6
    
def test_operand_addition():
    assert evaluat("94-") == 5
