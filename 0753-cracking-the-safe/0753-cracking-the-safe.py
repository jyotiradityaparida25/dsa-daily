class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()
        res = []
        
        def dfs(node: str):
            for x in range(k):
                edge = node + str(x)
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge[1:])
                    res.append(str(x))
                    
        start_node = "0" * (n - 1)
        dfs(start_node)
        
        return "".join(res) + start_node