class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        res=[[0]*n for _ in range(m)]
        temp=0
        
        for j in range(n):
            t1=-1
            for i in range(m):
                temp=matrix[i][j]
                t1=max(t1,temp)
            for i in range(m):
                if matrix[i][j]==-1:
                    matrix[i][j]=t1
        
        
        return matrix       