class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        l = [min(row) for row in matrix]
        
        l1 = []
        for j in range(n):
            mx = 0
            for i in range(m):
                mx = max(mx, matrix[i][j])
            l1.append(mx)
        
        return list(set(l) & set(l1))