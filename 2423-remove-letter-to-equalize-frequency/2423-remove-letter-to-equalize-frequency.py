class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            temp = word[:i] + word[i+1:]
            counts = Counter(temp).values()
            if len(set(counts)) == 1:
                return True
        return False