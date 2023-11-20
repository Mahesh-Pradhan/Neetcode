# 392. Is Subsequence

def isSubsequence(s,t):

    j=0

    for i in range(len(t)):
        if s[j]==t[i]:
            j+=1
    return j==len(s)