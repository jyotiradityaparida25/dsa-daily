class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_idx = nums.index(max_val)
        
        for i, num in enumerate(nums):
            if i != max_idx and num * 2 > max_val:
                return -1
                
        return max_idx