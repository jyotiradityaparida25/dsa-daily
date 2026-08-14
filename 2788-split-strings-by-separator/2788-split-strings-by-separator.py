class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        l1=[]
        for item in words:
            l=item.split(str(separator))
            for p in l:
                if p:
                    l1.append(p)
        return l1