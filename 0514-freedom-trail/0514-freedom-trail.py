class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_to_indices = collections.defaultdict(list)
        for i, char in enumerate(ring):
            char_to_indices[char].append(i)
            
        n = len(ring)
        memo = {}
        
        def dfs(ring_index: int, key_index: int) -> int:
           
            if key_index == len(key):
                return 0
                
            if (ring_index, key_index) in memo:
                return memo[(ring_index, key_index)]
                
            min_steps = float('inf')
            
            for target_index in char_to_indices[key[key_index]]:
                
                dist = abs(ring_index - target_index)
                min_dist = min(dist, n - dist)
                
                total_cost = min_dist + 1 + dfs(target_index, key_index + 1)
                
                min_steps = min(min_steps, total_cost)
                
            memo[(ring_index, key_index)] = min_steps
            return min_steps
            
        return dfs(0, 0)