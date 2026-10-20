class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        t=n//2
        if n>2:
            return nums[t]
        return -1