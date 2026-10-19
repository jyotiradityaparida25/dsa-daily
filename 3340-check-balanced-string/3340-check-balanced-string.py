class Solution:
    def isBalanced(self, num: str) -> bool:
        l=[int(c) for c in num]
        s=0
        for i in range(len(l)):
            if i%2==0:
                s+=l[i]
        return sum(l)-s==s