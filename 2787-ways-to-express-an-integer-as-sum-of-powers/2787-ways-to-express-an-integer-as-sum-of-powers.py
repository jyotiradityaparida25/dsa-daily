class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[0] = 1  
        
        max_base = int(n ** (1.0 / x)) + 1
        
        for base in range(1, max_base + 1):
            val = base ** x
            
            if val > n:
                break
                
            for i in range(n, val - 1, -1):
                dp[i] = (dp[i] + dp[i - val]) % MOD
                
        return dp[n]