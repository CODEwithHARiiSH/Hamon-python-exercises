from pyex import panagram



def test_Is_panagram():
    sentence = "abcdefghijklmnopqrstuvwxyz"
    assert panagram(sentence)

def test_Is_Not_panagram():
    sentence = "abcdefghijklmnopqrstuv"
    assert not panagram(sentence)
    
    
def test_null_Not_panagram():
    sentence = ""
    assert not panagram(sentence)
