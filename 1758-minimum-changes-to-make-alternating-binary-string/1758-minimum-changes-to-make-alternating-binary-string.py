class Solution:
    def minOperations(self, s: str) -> int:
        c1 = 0  
        
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                c1 += 1
          
        return min(c1, len(s) - c1)