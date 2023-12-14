# 1047. Remove All Adjacent Duplicates In String

def removeDuplicate(s):
    stack=[]

    for c in s:
        
        if stack:
            if stack[-1]==c:
                stack.pop()
            else:stack.append(c)
        else:
            stack.append(c)

    return ''.join(stack)

def removeDups(self, s: str) -> str:  # O(1) memory complexity
    idx =0
    while(idx+1<len(s)):
        if(s[idx]==s[idx+1]):
            s= s[:idx]+s[idx+2:]
            if idx > 0:
                idx -= 1
        else:
            idx += 1
    return s



s = "abbaca"
print(removeDuplicate(s))