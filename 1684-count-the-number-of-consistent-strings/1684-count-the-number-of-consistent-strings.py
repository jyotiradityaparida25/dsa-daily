class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)
        c = 0
        for w in words:
            if set(w).issubset(a):
                c += 1
        return c