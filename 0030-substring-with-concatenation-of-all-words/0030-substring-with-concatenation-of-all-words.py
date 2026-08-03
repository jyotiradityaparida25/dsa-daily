from collections import Counter
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        word_count = Counter(words)
        res = []
        
        for i in range(word_len):
            left = i
            right = i
            curr_count = Counter()
            words_seen = 0
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    curr_count[word] += 1
                    words_seen += 1
                    
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        words_seen -= 1
                        left += word_len
                        
                    if words_seen == num_words:
                        res.append(left)
                else:
                    curr_count.clear()
                    words_seen = 0
                    left = right
                    
        return res