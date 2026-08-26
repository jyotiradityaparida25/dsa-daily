class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        
        for i in range(len(names)):
            d[heights[i]] = names[i]
            
        sd = dict(sorted(d.items(), reverse=True))
        
        l = []
        for k, v in sd.items():
            l.append(v)
            
        return l