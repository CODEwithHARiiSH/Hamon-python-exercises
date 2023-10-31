    

#QUESTION 1. Write a python function called fizzbizz which will take a
    #    number n as input and print numbers i from 1 to n. 
    #     a. If i is divisible by 3, it will print fizz instead
    #        of i
    #     b. If i is divisible by 5, it will print bizz instead
    #        of i
    #     c. If i is divisible by 15, it will print fizzbizz
    #        instead i
    #     d. Otherwise, it will just print i

def fizzbizz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 != 0 and i % 15 != 0:
            print("fizz")
        elif i % 5 ==0 and i % 3 !=0 and i % 15 != 0:
            print("bizz")
        elif i % 15 ==0 and i % 3 ==0 and i % 5 == 0:
            print("fizzbizz")

        else:
            print(i)






# QUESTION2. Write a python function called palindrome that receives a string s as an
#    argument. It will return True if s is a palindrome and False if
#    not. A palindrome is a word that will read the same from left
#    to right and right to left. e.g. "dad", "abba"


def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
        







    # QUESTION3. Write a python function called panagram that receives a string s as an
    #    argument. It will return True if s is a panagram and False if
    #    not. A panagram is a sentence that contains all letters of the
    #    alphabet. e.g. "the quick brown fox jumps over the lazy dog"


def panagram(s):
    ansr=" "
    ref_string = 'abcdefghijklmnopqrstuvwxyz'
    for i in ref_string:
        if i in s:
            ansr=True
        else:
            ansr=False
            break
    return ansr
  
#myfunction=panagram(" ")
#print(myfunction)




    # QUESTION4. Write a function freq that will take a string s as input and
    #    return a dictionary. The keys of the dictionary will be the
    #    characters in s and the values will the number of times each of
    #    the characters occurs in s. Implement this without using the
    #    .count method of strings. (ie. s.count())

def freq(s):
    dicti={}
    for i in s:
        if i in dicti:
            dicti[i]+=1
        else:
            dicti[i]=1
    return dicti


if __name__ == '__main__':
    fizzbizz(30)
    b=palindrome("abba")
    c=panagram("the quick brown fox jumps over the lazy dog")
    d=freq("hallo")
    print(b)
    print(c)
    print(d)
    





