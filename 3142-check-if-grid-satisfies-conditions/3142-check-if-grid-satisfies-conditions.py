class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        row=len(grid)
        cols=len(grid[0])
        for i in range(row):
            for j in range(cols):
                if i + 1 < row and grid[i][j] != grid[i + 1][j]:
                    return False
                if j + 1 < cols and grid[i][j] == grid[i][j + 1]:
                    return False
        return True