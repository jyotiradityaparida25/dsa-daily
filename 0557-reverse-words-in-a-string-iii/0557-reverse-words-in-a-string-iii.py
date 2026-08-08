class Solution:
    def reverseWords(self, s: str) -> str:
        l=list(s.split())
        return ' '.join(word[::-1] for word in l)