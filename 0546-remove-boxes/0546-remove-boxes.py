class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        memo = {}

        def dp(i: int, j: int, k: int) -> int:
            if i > j:
                return 0
            
            while i < j and boxes[i] == boxes[i + 1]:
                i += 1
                k += 1

            key = (i, j, k)
            if key in memo:
                return memo[key]

            res = (k + 1) * (k + 1) + dp(i + 1, j, 0)

            for m in range(i + 1, j + 1):
                if boxes[m] == boxes[i]:
                    res = max(res, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))

            memo[key] = res
            return res

        return dp(0, len(boxes) - 1, 0)