class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        c,ms=0,0
        n=len(nums)
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                c+=1
                ms=max(ms,c)
            else:
                c=0
        return ms+1
        