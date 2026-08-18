class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        unique_chars = set(word1 + word2)
        
        for char in unique_chars:
            if abs(word1.count(char) - word2.count(char)) > 3:
                return False
                
        return True
