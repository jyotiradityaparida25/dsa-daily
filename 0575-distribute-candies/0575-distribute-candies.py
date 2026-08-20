class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s=set(candyType)
        n=len(candyType)//2
        return min(len(s),n)