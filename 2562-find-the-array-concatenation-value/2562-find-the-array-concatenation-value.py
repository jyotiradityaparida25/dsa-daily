class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            total += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        
        if left == right:
            total += nums[left]
        
        return total