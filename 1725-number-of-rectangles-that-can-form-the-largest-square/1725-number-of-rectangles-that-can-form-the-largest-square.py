class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        l=[]
        for r in rectangles:
            l.append(min(r))
        
        return l.count(max(l))
