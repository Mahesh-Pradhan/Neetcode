# 242. Valid Anagram

from collections import Counter # for func 3rd

    
def isanagram1(s, t): # in this approach we are counting the number of 
                            # each char in both string and then compare both the string.
    if len(s)!=len(t):
        return False
    counts1,counts2={},{}             # we will using hashmap to count and store the char count
    for i in range(len(s)):
        counts1[s[i]] = 1 + counts1.get(s[i],0)
        counts2[t[i]] = 1 + counts2.get(t[i],0)
    
    for c in counts1:
        if counts1[c]!=counts2.get(c,0):
            return False
    return True

def isAnagram2(s,t):# I this, we used a sorted() func which sorts strg and converts it 
    return sorted(s)==sorted(t)# to a list of chars in the string.


def isAnagram3(s,t):# Counter acts as a hashmap, which counts all the occurance of char in the strg 
    return Counter(s)== Counter(t)