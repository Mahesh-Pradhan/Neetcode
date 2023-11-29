# 2942. Find Words Containing Character

def findwordsContaining(words,x):

    res=[]

    for n,word in enumerate(words):
        for char in word:
            if char == x :
                res.append(n)
                break
    return res