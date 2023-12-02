# 1768. Merge Strings Alternately

def mergeAlternately(word1,word2):
    res=""
    i,j=0,0
    while i<len(word1) and j<len(word2):
        res+=word1[i]
        res+=word2[j]
        i+=1
        j+=1
    
    if len(word1)<len(word2):
        res+=word2[j:]
    else: res+=word1[i:]
    return res