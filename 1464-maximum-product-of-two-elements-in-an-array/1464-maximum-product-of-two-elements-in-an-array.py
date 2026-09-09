class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mp=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p=(nums[i]-1)*(nums[j]-1)
                mp=max(p,mp)
        return mp