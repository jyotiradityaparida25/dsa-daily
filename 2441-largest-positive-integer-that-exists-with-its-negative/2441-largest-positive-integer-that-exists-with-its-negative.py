class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        mx=-1
        t=-1
        for i in range(len(nums)):
            if nums[i] in nums and -nums[i] in nums:
                t=nums[i]
            mx=max(mx,t)
        return mx