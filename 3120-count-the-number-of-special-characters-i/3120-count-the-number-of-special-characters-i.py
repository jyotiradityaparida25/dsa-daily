class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        words=set(word)
        c=0
        for ch in words:
            if ch.islower() and ch.upper() in words:
                c+=1
        return c
        