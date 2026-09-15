class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        max_sum = float('-inf')

        for L in range(cols):
            row_sums = [0] * rows
            for R in range(L, cols):
               
                for i in range(rows):
                    row_sums[i] += matrix[i][R]

                prefix_sums = [0]
                curr_sum = 0
                for val in row_sums:
                    curr_sum += val
                  
                    target = curr_sum - k
                    idx = bisect.bisect_left(prefix_sums, target)
                    if idx < len(prefix_sums):
                        max_sum = max(max_sum, curr_sum - prefix_sums[idx])
                    
                    bisect.insort(prefix_sums, curr_sum)

        return max_sum