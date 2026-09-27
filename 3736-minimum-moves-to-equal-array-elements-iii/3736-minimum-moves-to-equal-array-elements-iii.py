class Solution:
    def minMoves(self, nums: List[int]) -> int:
        c=0
        mx=max(nums)
        for n in nums:
            if n<mx:
                c+=mx-n
        return c