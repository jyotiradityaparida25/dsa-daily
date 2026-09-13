class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def wordSum(word):
            res=''
            for w in word:
                res+=w
            return res
        
        return wordSum(word1)==wordSum(word2)