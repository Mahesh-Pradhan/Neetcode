# 1. Two Sum
# [2,7,11,15]

def twoSum(nums,target):
    hashmap={}

    for i,n in enumerate(nums):
        res=target-n # 9-2=7
        if res in hashmap:
            return [hashmap[res],i]
        hashmap[n]=i

arr=[2,7,11,15]
target=18
print(twoSum(arr,target))

