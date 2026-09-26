from collections import deque

class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        m, n = len(forest), len(forest[0])
        trees = []
        for r in range(m):
            for c in range(n):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
        
        trees.sort()

        def bfs(sr: int, sc: int, tr: int, tc: int) -> int:
            queue = deque([(sr, sc, 0)])
            visited = {(sr, sc)}
            while queue:
                r, c, d = queue.popleft()
                if r == tr and c == tc:
                    return d
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and forest[nr][nc] != 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, d + 1))
            return -1

        curr_r, curr_c = 0, 0
        total_steps = 0

        for _, tr, tc in trees:
            steps = bfs(curr_r, curr_c, tr, tc)
            if steps == -1:
                return -1
            total_steps += steps
            curr_r, curr_c = tr, tc

        return total_steps