class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        l1=[]
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                l1.append(nums[i])
        return l1