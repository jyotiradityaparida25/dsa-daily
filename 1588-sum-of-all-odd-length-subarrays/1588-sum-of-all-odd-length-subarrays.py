class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        total = 0
        for length in range(1, n + 1, 2):
            for start in range(n - length + 1):
                total += sum(arr[start:start + length])
        return total