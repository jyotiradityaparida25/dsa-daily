import collections

class Solution:
    def canDistribute(self, nums: list[int], quantity: list[int]) -> bool:
        counts = list(collections.Counter(nums).values())
        quantity.sort(reverse=True)
        
        m = len(quantity)
        subset_sum = [0] * (1 << m)
        for i in range(1 << m):
            for j in range(m):
                if (i >> j) & 1:
                    subset_sum[i] += quantity[j]

        n_counts = len(counts)
        dp = [[False] * (1 << m) for _ in range(n_counts + 1)]
        dp[0][0] = True

        for i in range(n_counts):
            count = counts[i]
            for mask in range(1 << m):
                if not dp[i][mask]:
                    continue
                
                dp[i + 1][mask] = True
                
                submask = ((1 << m) - 1) ^ mask
                sub = submask
                while sub > 0:
                    if subset_sum[sub] <= count:
                        dp[i + 1][mask | sub] = True
                    sub = (sub - 1) & submask

        return dp[n_counts][(1 << m) - 1]