class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    is_pal[i][j] = (j - i <= 2) or is_pal[i + 1][j - 1]
                    
        for i in range(1, n - 1):
            if not is_pal[0][i - 1]:
                continue
            for j in range(i, n - 1):
                if is_pal[i][j] and is_pal[j + 1][n - 1]:
                    return True
                    
        return False