class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        start = 0
        n = len(s)
        
        for i in range(n):

            if i == n - 1 or s[i] != s[i + 1]:
                
                if i - start + 1 >= 3:
                    res.append([start, i])
                    
                start = i + 1
                
        return res