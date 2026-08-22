class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        unique_sum = sum(set(nums))
        duplicate = sum(nums) - unique_sum
        missing = (n * (n + 1)) // 2 - unique_sum
        return [duplicate, missing]