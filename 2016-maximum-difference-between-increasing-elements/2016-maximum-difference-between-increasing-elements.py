class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        mx=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    d=nums[j]-nums[i]
                    mx=max(mx,d)
        return mx