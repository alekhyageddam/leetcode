class Solution:
    #one pass approach to buy and sell stock
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float("inf")
        maxprofit = 0 #the max difference between selling price and min price
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit