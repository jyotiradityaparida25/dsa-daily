class Solution:
    def sortSentence(self, s: str) -> str:
        l=s.split()
        l.sort(key=lambda w:int(w[-1]))
        return " ".join(c[:-1] for c in l)
