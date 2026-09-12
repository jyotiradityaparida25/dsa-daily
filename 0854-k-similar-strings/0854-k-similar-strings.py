class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
            
        queue = deque([(s1, 0)])
        visited = {s1}
        
        while queue:
            curr, step = queue.popleft()
            if curr == s2:
                return step
                
            i = 0
            while curr[i] == s2[i]:
                i += 1
                
            for j in range(i + 1, len(curr)):
                if curr[j] == s2[i] and curr[j] != s2[j]:
                    next_str = list(curr)
                    next_str[i], next_str[j] = next_str[j], next_str[i]
                    next_str_str = "".join(next_str)
                    
                    if next_str_str not in visited:
                        if next_str_str == s2:
                            return step + 1
                        visited.add(next_str_str)
                        queue.append((next_str_str, step + 1))