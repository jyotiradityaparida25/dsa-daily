class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        l=list(text.split())
        l1=[]
        for i in range(2,len(l)):
            if l[i-2]==first and l[i-1]==second:
                l1.append(l[i])
        return l1