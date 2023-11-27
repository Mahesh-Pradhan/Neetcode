#724. Find Pivot Index

def pivotindex(nums):

    total=sum(nums)
    leftsum=0

    for i in range(len(nums)-1):

        rightsum=total-nums[i]-leftsum

        if rightsum==leftsum:
            return i
        leftsum+=nums[i]
    return -1