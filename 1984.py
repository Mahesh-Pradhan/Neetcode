# 1984. Minimum Difference Between Highest and Lowest of K Scores

def min_diff(nums,k):
    nums.sort()
    i,j=0,k-1
    res=float("inf")
    while j<len(nums):
        res=min(res,nums[j]-nums[i])
        i+=1
        j+=1
    return res
