    

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
    n=int(input("enter the number :  "))
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 != 0 and i % 15 != 0:
            print("fizz")
        elif i % 5 ==0 and i % 3 !=0 and i % 15 != 0:
            print("bizz")
        elif i % 15 ==0 and i % 3 ==0 and i % 5 == 0:
            print("fizzbizz")

        else:
            print(i)



fizzbizz(" ") 
