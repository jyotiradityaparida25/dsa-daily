class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        for num in nums:
            if nums.count(num)>2:
                return False
        return True 
