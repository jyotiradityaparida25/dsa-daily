from typing import List
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        
        @cache
        def backtrack(start: int) -> List[str]:
            if start == len(s):
                return [""]
            
            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for tail in backtrack(end):
                        if tail:
                            res.append(word + " " + tail)
                        else:
                            res.append(word)
            return res
            
        return backtrack(0)