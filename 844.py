# 844. Backspace String Compare

def backSpaceCompare(s,t):
    slist=[]
    tlist=[]

    for i in s:
        if i=="#":
            if slist:
                slist.pop()
        else:
            slist.append(i)
              
    for i in s:
        if i=="#":
            if tlist:
                slist.pop()
        else:
            slist.append(i)

              
    return slist==tlist