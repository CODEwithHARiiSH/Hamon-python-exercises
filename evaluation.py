def evaluat(x):
    stack=[]
    for i in x:
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
    
    
