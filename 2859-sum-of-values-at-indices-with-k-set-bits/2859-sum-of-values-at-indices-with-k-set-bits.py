class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s1=0
        s=''
        for i in range(len(nums)):
            s=str(bin(i))
            if s.count(str(1))==k:
                s1+=nums[i]
        
        return s1