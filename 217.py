# 217. Contains Duplicate

def checkduplicate(nums):# In this approch we use nested for loop for check whether  a number is present in the array
    for i in range(len(nums)): # due to nested forr loop the time complexity becomes Big(O)- n^2, which is not good.
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False


def checkDuplicate(nums): # In this we use a set() Function to keep the elemnts in the set. Set() does'nt store duplicates
    check=set()

    for i in nums:
        if i in check:# If elements is present in the set(), we return True as duplicate found.
            return True
        check.add(i) # Else we add the current number to the set.
    return False

def checkdUplicate(nums):
    pass # WE can sort the array and then compare each element with its corresponding element(1st and 2nd or 5thand 6th)till 
                # the array ends.