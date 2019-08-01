def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    minprice = float('inf')
    maxprofit = 0
    for i in prices:
        minprice = min(minprice,i)
        profit = i - minprice
        maxprofit = max(maxprofit,profit)
    return maxprofit
if __name__ == "__main__":
    nums = [7,1,5,3,6,4]
    p = maxProfit(nums)
    print(p)