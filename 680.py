# 680. Valid Palindrome II

def validPalindrome(s):
    i,j=0,len(s)-1

    while i<j:

        if s[i]!=s[j]:
            leftstr,rightstr=s[i+1:j+1],rightstr[i:j]
            return (leftstr==leftstr[::-1]) or rightstr==rightstr[::-1]
        i+=1
        j-=1
    return True