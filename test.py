import unittest
from pyex import freq, palindrome


class Testpalindrome(unittest.TestCase):
    
    def testPalindromeself(self):
        sentence = "dad"
        self.assertTrue(palindrome(sentence))

    
    def testIsNotPalindrome(self):
        sentence = "dada"
        self.assertFalse(palindrome(sentence))
    
    def testIsnullPalindrome(self):
        sentence = ""
        self.assertTrue(palindrome(sentence))
        


class Testfreq(unittest.TestCase):
    
    def testIsFreq(self):
        sentence = "hallo"
        exp_output={"a":1 , "l":2 , "h":1 , "o":1}
        self.assertDictEqual(exp_output,freq(sentence))
        
        
        


if __name__ == "__main__":
    unittest.main()
