# 303. Range Sum Query - Immutable



class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        cur=0
        for i in nums:
            cur+=i
            self.prefix.append(cur)
        

    def sumRange(self, left: int, right: int) -> int:
        rightsum=self.prefix[right]
        leftsum=self.prefix[left-1] if left>0 else 0
        return rightsum-leftsum 