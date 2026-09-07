class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = dict(zip(sorted(set(arr)), range(1, len(set(arr)) + 1)))
        return [ranks[x] for x in arr]
        