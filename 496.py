# 496. Next Greater Element I

def nextGreaterElement(nums1,nums2):

    map={}
    res=[]

    for i in range(len(nums2)-1):

        if nums2[i] in nums1:

            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    map[nums2[i]]=nums2[j]
                    break
    for i in nums1:
        if i in map:
            res.append(map[i])
        else: res.append(-1)
    return res

    