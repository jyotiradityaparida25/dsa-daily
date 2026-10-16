class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        
        sums = [0] * (n - k + 1)
        curr_sum = sum(nums[:k])
        sums[0] = curr_sum
        
        for i in range(1, n - k + 1):
            curr_sum += nums[i + k - 1] - nums[i - 1]
            sums[i] = curr_sum

        m = len(sums)
        
        left = [0] * m
        best_left = 0
        for i in range(m):
            if sums[i] > sums[best_left]:
                best_left = i
            left[i] = best_left

        right = [0] * m
        best_right = m - 1
        for i in range(m - 1, -1, -1):
            if sums[i] >= sums[best_right]:
                best_right = i
            right[i] = best_right

        max_total = -1
        ans = [-1, -1, -1]

        for j in range(k, m - k):
            l = left[j - k]
            r = right[j + k]
            total = sums[l] + sums[j] + sums[r]

            if total > max_total:
                max_total = total
                ans = [l, j, r]

        return ans