# 49. Group Anagrams

from collections import defaultdict


def groupanagrams(strs):
    res=defaultdict(list)
    for s in strs:

        count = [0]*26

        for c in s:
            count[ord[c]-ord["a"]]+=1

        res[tuple(count)].append(s)
    return res.values()