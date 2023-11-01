from evaluation import *

def test_single_operator():
    assert evaluat("9") == 9
    
def test_operand_addition():
    assert evaluat("94+") == 13
    
def test_operand_minus():
    assert evaluat("94-") == 5
    
def test_operand_multiplication():
    assert evaluat("94*") == 36

def test_operand_division():
    assert evaluat("93*") == 3
