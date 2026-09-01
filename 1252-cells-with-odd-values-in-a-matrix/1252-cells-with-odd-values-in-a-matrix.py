class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        grid=[[0]*n for _ in range(m)]
        def incrow(mat,k):
                for j in range(n):
                    mat[k][j]+=1
        
        def inccol(mat,k):
                for i in range(m):
                    mat[i][k]+=1

        for ind in indices:
            incrow(grid,ind[0])
            inccol(grid,ind[1])
        
        c=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]%2!=0:
                    c+=1
        
        return c