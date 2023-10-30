    # 3. Write a python function called panagram that receives a string s as an
    #    argument. It will return True if s is a panagram and False if
    #    not. A panagram is a sentence that contains all letters of the
    #    alphabet. e.g. "the quick brown fox jumps over the lazy dog"


def panagram(s):
    s=input("enter your sentence : ")
    ansr=" "
    ref_string = 'abcdefghijklmnopqrstuvwxyz '
    for i in ref_string:
        if i in s:
            ansr=True
        else:
            ansr=False
            break
    return ansr
  
myfunction=panagram(" ")
print(myfunction)






