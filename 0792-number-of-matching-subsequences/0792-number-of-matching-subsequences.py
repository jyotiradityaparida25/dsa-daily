import collections
from typing import List
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = collections.defaultdict(list)
        for it in map(iter, words):
            waiting[next(it)].append(it)
            
        count = 0
        for char in s:
            for it in waiting.pop(char, ()):
                try:
                    waiting[next(it)].append(it)
                except StopIteration:
                    count += 1
        return count