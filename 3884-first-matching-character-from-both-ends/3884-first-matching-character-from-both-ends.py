class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        l=[]
        n=len(s)
        for i in range(n):
            if s[i]==s[n-i-1]:
                l.append(i)
        l.sort()
        if len(l)>0:
            return l[0]
        return -1