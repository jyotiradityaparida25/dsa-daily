class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        freq1 = Counter(words1)
        freq2 = Counter(words2)
        
        return sum(1 for word, count in freq1.items() if count == 1 and freq2[word] == 1)