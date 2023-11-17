# 1299. Replace Elements with Greatest Element on Right Side

def replaceElements(arr):
    right_max=-1

    for i in range(len(arr)-1,-1,-1):
        current=arr[i]
        arr[i]=right_max
        right_max=max(right_max,current)
    return arr