class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing = True
        is_decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                is_decreasing = False
            if nums[i] < nums[i - 1]:
                is_increasing = False
                
        return is_increasing or is_decreasing