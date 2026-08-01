class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        li=list(s)
        l=len(s)
        for i in range(0,l,2*k):
            left=i
            right=min(i+k-1,l-1)
            while left<right:
                li[left],li[right]=li[right],li[left]
                left+=1
                right-=1
        return "".join(li)