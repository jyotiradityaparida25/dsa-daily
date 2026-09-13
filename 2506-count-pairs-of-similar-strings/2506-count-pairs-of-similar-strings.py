class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq = Counter(frozenset(w) for w in words)
        return sum(count * (count - 1) // 2 for count in freq.values())