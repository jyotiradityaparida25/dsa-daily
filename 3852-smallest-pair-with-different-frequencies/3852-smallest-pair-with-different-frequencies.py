from collections import Counter

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        vals = sorted(freq)

        x = vals[0]
        for y in vals[1:]:
            if freq[y] != freq[x]:
                return [x, y]
        return [-1, -1]