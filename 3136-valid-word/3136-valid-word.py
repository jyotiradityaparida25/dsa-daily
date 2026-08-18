class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        if not word.isalnum():
            return False
        v=set('aeiouAEIOU')
        hv,hc=False,False
        for c in word:
            if c.isalpha():
                if c in v:
                    hv=True
                else:
                    hc=True
        return hc and hv