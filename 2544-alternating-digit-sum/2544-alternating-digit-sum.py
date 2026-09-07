class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l=[int(d) for d in str(n)]
        s=0
        for i in range(len(l)):
            if i%2==0:
                s+=l[i]
            else:
                s+=-l[i]
        return s