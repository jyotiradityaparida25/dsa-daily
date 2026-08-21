class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_counts = [0] * 26
        for char in letters:
            letter_counts[ord(char) - ord('a')] += 1
            
        def backtrack(i):
            if i == len(words):
                return 0
                
            max_score = backtrack(i + 1)
            
            word = words[i]
            word_score = 0
            is_valid = True
            
            for char in word:
                idx = ord(char) - ord('a')
                letter_counts[idx] -= 1
                word_score += score[idx]
                if letter_counts[idx] < 0:
                    is_valid = False
                    
            if is_valid:
                max_score = max(max_score, word_score + backtrack(i + 1))
                
            for char in word:
                idx = ord(char) - ord('a')
                letter_counts[idx] += 1
                
            return max_score
            
        return backtrack(0)