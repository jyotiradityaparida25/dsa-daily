class Solution:
    def sumZero(self, n: int) -> List[int]:
        pos = 1
        neg = -1
        l = []
        
        if n % 2 == 1:
            l.append(0)
            
        for i in range(n // 2):
            l.append(pos)
            l.append(neg)
            
            pos += 1
            neg -= 1

        return l