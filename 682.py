# 682. Baseball Game

def calPoints(operations):
    stack=[]
    s=0
    while s<len(operations):
        if operations[s]=="C":
            stack.pop()        
        elif operations[s]=="D":
            stack.append(2*stack[-1])
        elif operations[s]=="+":
            stack.append(stack[-1]+stack[-2])
        else:
            stack.append(int(operations[s]))    
        s+=1
    return sum(stack)

