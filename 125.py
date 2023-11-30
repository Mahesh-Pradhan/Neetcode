# 125. Valid Palindrome

def isPalindrome(s):

    left,right=0,0

    while left<right:
        while left<right and  not valid(s[left]):
            left+=1
        while left<right and  not valid(s[right]):
            right+=1
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

def valid(s):
    return (ord('A')<= ord(s)<=ord('Z') or ord('a')<= ord(s)<=ord('z') or ord('0')<= ord(s)<=ord('9'))
