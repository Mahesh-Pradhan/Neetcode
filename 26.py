# 26. Remove Duplicates from Sorted Array

def removedupliacates(nums):

    left = 1

    for right in range(1,len(nums)):# left and right pointer are initialized at index 1

        if nums[right]!=nums[right-1]: # if the consecutive numbers are not same, then we know the there is a new number
            nums[left]=nums[right]     # we swap them with left pointer index and increament it
            left += 1
    return left # return the number of distinct elements.