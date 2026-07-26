from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s.lower()
        # t.lower()
        # a=list(s)
        # b=list(t)
        # a.sort()
        # b.sort()
        x=Counter(s)
        y=Counter(t)
        # if len(s)==len(t) and a==b and x==y:
        if x==y:
            return True
        return False