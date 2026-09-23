class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        total_count = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count_j = dp[j][diff]
                total_count += count_j
                dp[i][diff] += count_j + 1

        return total_count