# 121. Best Time to Buy and Sell Stock

def maxProfit(prices):

    left,right=0,1
    maxP=0
    while right<len(prices):
        if prices[left]<prices[right]:
            profit=prices[right]-prices[left]
            maxP=max(profit,maxP)
        else:
            left=right # else the left pointer is greater than the right pointer
        right +=1
    return maxP

