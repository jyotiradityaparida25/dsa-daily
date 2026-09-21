class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        words = text.split()
        cnt = 0
        
        for word in words:
            if not any(char in broken_set for char in word):
                cnt += 1
                
        return cnt