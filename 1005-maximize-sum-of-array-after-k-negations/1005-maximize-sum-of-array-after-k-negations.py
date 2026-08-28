class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        n = len(nums)
    
        while i < n and nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1
    
        total = sum(nums)
    
        if k % 2 == 1:
            total -= 2 * min(nums)
    
        return total