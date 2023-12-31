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
    assert evaluat("93/") == 3

def test_minus_1():
    assert evaluat("39-") == -6

def test_three_operands():
    assert evaluat("93+6*") == 72
    
def test_three_operands_1():
    assert evaluat("93-6*6-") == 30
def test_alphabet():
    assert evaluat("aa66+") == 12

def test_only_alphabets():
    assert evaluat("aa") == "Invalid Inputs"
