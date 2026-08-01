class Solution:
    def possibleStringCount(self, word: str) -> int:
        l=list(word)
        n=len(l)
        count=0
        for i in range(1,n):
            if l[i-1]==l[i]:
                count+=1
        return count+1