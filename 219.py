# 219. Contains Duplicate II

def containsDuplicate(nums,k):
    present=set()
    left=0

    for r in range(len(nums)):
        if r - left > k :
            present.remove(nums[left])
            left+=1
        if nums[r] in present  :
            return True
        present.add(nums[r])
    return False