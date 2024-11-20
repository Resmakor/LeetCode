class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, profit = prices[0], 0
        for price in prices[1:]:
            if buy > price:
                buy = price
            if price - buy > profit:
                profit = price - buy
        return profit