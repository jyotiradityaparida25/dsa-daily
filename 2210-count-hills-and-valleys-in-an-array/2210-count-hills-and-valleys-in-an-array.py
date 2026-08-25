class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        left = nums[0]
        
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
                
            if left < nums[i] > nums[i + 1]:
                count += 1
            elif left > nums[i] < nums[i + 1]:
                count += 1
                
            left = nums[i]
            
        return count