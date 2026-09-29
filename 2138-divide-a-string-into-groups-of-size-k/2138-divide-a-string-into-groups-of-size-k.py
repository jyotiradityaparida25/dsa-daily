class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        l=[]
        for i in range(0,len(s),k):
            l1=s[i:i+k]
            if len(l1)<k:
                l1=l1+fill*(k-len(l1))
            l.append(l1)
        return l