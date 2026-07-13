class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        path = []

        def dfs(open_cnt, close_cnt):
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            if open_cnt < n:
                path.append("(")
                dfs(open_cnt + 1, close_cnt)
                path.pop()

            if close_cnt < open_cnt:
                path.append(")")
                dfs(open_cnt, close_cnt + 1)
                path.pop()

        dfs(0, 0)
        return res