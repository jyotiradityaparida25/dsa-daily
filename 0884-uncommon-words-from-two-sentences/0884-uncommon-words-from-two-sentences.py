class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        r=(s1+' '+s2).split()
        c=Counter(r)
        l=[]
        for k,v in c.items():
            if v==1:
                l.append(k)
        return l