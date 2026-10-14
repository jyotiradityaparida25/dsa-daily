import collections

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        adj = collections.defaultdict(list)
        indegree = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
            
        queue = collections.deque([i for i in range(n) if indegree[i] == 0])
        dp = [[0] * 26 for _ in range(n)]
        
        for i in range(n):
            dp[i][ord(colors[i]) - ord('a')] = 1
            
        visited_nodes = 0
        ans = 0
        
        while queue:
            node = queue.popleft()
            visited_nodes += 1
            ans = max(ans, max(dp[node]))
            
            for neighbor in adj[node]:
                for c in range(26):
                    dp[neighbor][c] = max(
                        dp[neighbor][c],
                        dp[node][c] + (1 if ord(colors[neighbor]) - ord('a') == c else 0)
                    )
                
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return ans if visited_nodes == n else -1