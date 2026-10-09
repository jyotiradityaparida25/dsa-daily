class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        l=[]
        for s in sentences:
            x=s.split()
            l.append(len(x))
        l.sort()
        return l[-1]