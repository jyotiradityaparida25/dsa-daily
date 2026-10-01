class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        mn=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                m=abs(i-start)
                mn=min(m,mn)
        return mn