class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        for i in range(n):
            c=s[i]
            s1=s[i+1:]
            if c not in s1 and s.count(c)==1:
                return i
        return -1