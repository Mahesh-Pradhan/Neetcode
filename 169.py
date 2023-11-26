# 169. Majority Element

def maj(nums):
    """       This can be solved by sort the array and returning middle element. 
    nums.sort()
    return nums[len(nums)//2]
    """

    # using hashmap

    count={}
    ma=0
    ele=0

    for i in nums:

        count[i]=1+count.get(i,0)

        if count[i]>ma:
            ele=i
            ma=count[i]

    return ele