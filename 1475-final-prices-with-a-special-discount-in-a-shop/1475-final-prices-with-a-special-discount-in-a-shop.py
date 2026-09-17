class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        res = prices.copy()
        
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prev_idx = stack.pop()
                res[prev_idx] -= prices[i]
            stack.append(i)
            
        return res