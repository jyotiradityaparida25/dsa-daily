class Solution:
    def reverseVowels(self, s: str) -> str:
        n=len(s)
        li=list(s)
        r=n-1
        l=0
        l1=['a','e','i','o','u','A','E','I','O','U']
        while l<=r:
            if li[l] not in l1:
                l+=1
            elif li[r] not in l1:
                r-=1
            else:
                li[l],li[r]=li[r],li[l]
                l+=1
                r-=1
        return "".join(li)
            