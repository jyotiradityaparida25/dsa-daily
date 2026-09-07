class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = sum(int(d) for num in nums for d in str(num))
        return abs(s1 - s2)