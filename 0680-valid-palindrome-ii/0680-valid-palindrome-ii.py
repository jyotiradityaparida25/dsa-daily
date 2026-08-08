class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        c=0
        while l<r:
            if s[l]!=s[r]:
                sl=s[l+1:r+1]
                sr=s[l:r]
                return sl==sl[::-1] or sr==sr[::-1]
            l+=1
            r-=1
        return True