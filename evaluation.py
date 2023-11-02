def evaluat(x):
    stack=[]
    try:
            for i in x:
                char='abcdefghijklmnopqrstuvwxizABCDEFGHIJKLMNOPQRSTUVWXYZ'
                if i in char:
                    continue
                else:
                    if i in ["+" , "-" , "*" , "/"]:
                        operand_1=stack.pop()
                        operand_2=stack.pop()
                    if i == "+":
                        stack.append(operand_1+operand_2)
                    elif i == "-":
                        stack.append(operand_2-operand_1)
                    elif i == "*":
                        stack.append(operand_1*operand_2)
                    elif i == "/":
                        stack.append(operand_2//operand_1)

                    else:
                        stack.append(int(i))
            return stack.pop()
    except:
        return "Invalid Inputs"


    
    
    
    
if __name__ == '__main__':
    print(evaluat("aa"))
    
