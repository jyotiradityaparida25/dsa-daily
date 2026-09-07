class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        p=n*n
        if p*w>maxWeight:
            return maxWeight//w
        return p