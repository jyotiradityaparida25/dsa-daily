class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        li=list(s)
        n=len(s)
        left=0
        right=n-1
        while left<right:
            if not li[left].isalpha():
                left+=1
            elif not li[right].isalpha():
                right-=1
            else:
                li[left],li[right]=li[right],li[left]
                left+=1
                right-=1
        return "".join(li)