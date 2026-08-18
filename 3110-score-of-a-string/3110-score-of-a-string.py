class Solution:
    def scoreOfString(self, s: str) -> int:
        n=len(s)
        l=[]
        for i in range(1,n):
            l.append(abs(ord(s[i-1])-ord(s[i])))
        return sum(l)