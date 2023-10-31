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


if __name__ == "__main__":
    unittest.main()
