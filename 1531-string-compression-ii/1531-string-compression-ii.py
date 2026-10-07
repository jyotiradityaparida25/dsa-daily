import functools

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def calc_length(count: int) -> int:
            if count <= 1:
                return count
            if count < 10:
                return 2
            if count < 100:
                return 3
            return 4

        @functools.lru_cache(None)
        def dp(i: int, k_left: int) -> int:
            if k_left < 0:
                return float('inf')
            if i >= len(s) or len(s) - i <= k_left:
                return 0

            res = dp(i + 1, k_left - 1)
            
            same_count = 0
            diff_count = 0
            
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    same_count += 1
                else:
                    diff_count += 1
                
                if k_left - diff_count < 0:
                    break
                    
                res = min(res, calc_length(same_count) + dp(j + 1, k_left - diff_count))

            return res

        return dp(0, k)