class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        s=0
        for n in nums:
            if nums.count(n)==1:
                s+=n
        return s