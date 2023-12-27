# 1578. Minimum Time to Make Rope Colorful

def minCost(colors, neededTime):
    # If two adjacent balloons have same color then pop the one with least time.
    
    l=res =0
    for r in range(1,len(neededTime)):
        if colors[l]==colors[r]:
            if neededTime[l]<neededTime[r]:
                res+=neededTime[l]
                l=r
            else:
                res+=neededTime[r]
        else:
            l=r

    return res

