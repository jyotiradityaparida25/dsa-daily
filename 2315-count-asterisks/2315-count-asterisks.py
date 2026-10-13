class Solution:
    def countAsterisks(self, s: str) -> int:
        c=0
        ib=False
        for ch in s:
            if ch=='|':
                ib=not ib
            elif ch=='*' and not ib:
                c+=1
        return c