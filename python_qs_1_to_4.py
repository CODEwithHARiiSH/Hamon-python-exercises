    # 2. Write a python function called palindrome that receives a string s as an
    #    argument. It will return True if s is a palindrome and False if
    #    not. A palindrome is a word that will read the same from left
    #    to right and right to left. e.g. "dad", "abba"


def palindrome(s):
    s=input("enter a word  :  ")
    if s == s[::-1]:
        print("True")
    else:
        print("False")


palindrome('')
