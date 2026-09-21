class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c=s.count(s[0])
        for i in range(len(s)):
            if s.count(s[i])!=c:
                return False
        return True