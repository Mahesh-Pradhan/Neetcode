# 14. Longest Common Prefix

def longestcommonprefix(strs):
    res = ""

    for i in range(len(strs)):
        for s in strs:
            if i==len(s) or s[i]!=strs[0][i]:
                return res
        res+=strs[0][i]
    return res

