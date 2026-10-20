class Solution:
    def reverseDegree(self, s: str) -> int:
        l=[c for c in s]
        s=0
        for i in range(len(l)):
            s+=(123-ord(l[i]))*(i+1)
        return s