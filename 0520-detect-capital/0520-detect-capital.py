class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count=sum(1 for ch in word if ch.isupper())
        if count==len(word):
            return True
        if count==0:
            return True
        if count==1 and word[0].isupper():
            return True
        return False
        

            