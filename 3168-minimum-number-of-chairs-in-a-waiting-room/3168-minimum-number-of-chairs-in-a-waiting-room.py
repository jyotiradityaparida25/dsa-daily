class Solution:
    def minimumChairs(self, s: str) -> int:
        c=0
        mc=float('-inf')
        for i in range(len(s)):
            if s[i]=='E':
                c+=1
            else:
                c-=1
            mc=max(c,mc)
        return mc