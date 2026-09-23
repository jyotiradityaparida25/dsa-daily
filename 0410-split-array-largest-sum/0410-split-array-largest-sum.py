class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        def count_subarrays(max_allowed_sum: int) -> int:
            count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > max_allowed_sum:
                    count += 1
                    current_sum = num
                else:
                    current_sum += num
            return count

        ans = high
        while low <= high:
            mid = (low + high) // 2
            if count_subarrays(mid) <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans