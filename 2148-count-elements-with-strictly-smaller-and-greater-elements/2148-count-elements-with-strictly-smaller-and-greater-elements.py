class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        mx=nums[-1]
        mn=nums[0]
        c=0
        for i in range(len(nums)):
            if nums[i]<mx and nums[i]>mn:
                c+=1
        return c