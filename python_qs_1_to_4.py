    # 4. Write a function freq that will take a string s as input and
    #    return a dictionary. The keys of the dictionary will be the
    #    characters in s and the values will the number of times each of
    #    the characters occurs in s. Implement this without using the
    #    .count method of strings. (ie. s.count())

def freq(s):
    s=input("enter your line : ")
    dicti={}
    for i in s:
        if i in dicti:
            dicti[i]+=1
        else:
            dicti[i]=1
    return dicti
a=freq("")
print(a)
print(type(a))







