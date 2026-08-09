class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")
            
        words = paragraph.lower().split()
        banned_set = set(banned)
        
        word_counts = {}
        for word in words:
            if word not in banned_set:
                word_counts[word] = word_counts.get(word, 0) + 1
                
        return max(word_counts, key=word_counts.get)