class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cuts = [i - 1 for i in range(n + 1)]
        
        for i in range(n):
            j = 0
            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                if 1 + cuts[i - j] < cuts[i + j + 1]:
                    cuts[i + j + 1] = 1 + cuts[i - j]
                j += 1
                
            j = 0
            while i - j >= 0 and i + j + 1 < n and s[i - j] == s[i + j + 1]:
                if 1 + cuts[i - j] < cuts[i + j + 2]:
                    cuts[i + j + 2] = 1 + cuts[i - j]
                j += 1
                
        return cuts[-1]