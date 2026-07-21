class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_cost1 = float('inf')
        profit1 = 0
        min_cost2 = float('inf')
        profit2 = 0
        
        for price in prices:
            min_cost1 = min(min_cost1, price)
            profit1 = max(profit1, price - min_cost1)
            min_cost2 = min(min_cost2, price - profit1)
            profit2 = max(profit2, price - min_cost2)
            
        return profit2
        