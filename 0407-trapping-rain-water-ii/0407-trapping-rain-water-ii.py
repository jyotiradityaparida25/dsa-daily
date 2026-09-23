class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        pq = []

        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    heapq.heappush(pq, (heightMap[r][c], r, c))
                    visited[r][c] = True

        trapped_water = 0
        max_height = 0

        while pq:
            height, r, c = heapq.heappop(pq)
            max_height = max(max_height, height)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    if heightMap[nr][nc] < max_height:
                        trapped_water += max_height - heightMap[nr][nc]
                    heapq.heappush(pq, (heightMap[nr][nc], nr, nc))

        return trapped_water