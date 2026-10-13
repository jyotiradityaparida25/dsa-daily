class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        n=len(pref)
        c=0
        for w in words:
            if pref in w and w[:n]==pref:
                c+=1
        return c