class Solution:
    def findGCD(self, nums: list[int]) -> int:
        nums.sort()
        mn=nums[0]
        mx=nums[-1]
        m=-1
        mx1=-1
        for i in range(1,mx+1):
            if mn%i==0 and mx%i==0:
                m=i
            mx1=max(m,mx1)
        
        return mx1