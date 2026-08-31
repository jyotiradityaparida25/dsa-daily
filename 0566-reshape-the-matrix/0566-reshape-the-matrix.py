class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        if m*n!=r*c:
            return mat
        row,col=0,0
        res=[[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                res[i][j]=mat[row][col]
                col+=1
                if col==n:
                    col=0
                    row+=1
        return res