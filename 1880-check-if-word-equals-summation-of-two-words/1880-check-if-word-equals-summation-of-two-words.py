class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def wordToNum(word):
            digits = ''.join(str(ord(c) - 97) for c in word)
            return int(digits)
        
        return wordToNum(firstWord) + wordToNum(secondWord) == wordToNum(targetWord)