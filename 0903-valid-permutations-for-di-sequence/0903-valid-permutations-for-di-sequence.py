class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [1] * (n + 1)
        
        for i, ch in enumerate(s):
            new_dp = [0] * (n - i)
            if ch == 'I':
                curr_sum = 0
                for j in range(n - i):
                    curr_sum = (curr_sum + dp[j]) % MOD
                    new_dp[j] = curr_sum
            else:
                curr_sum = 0
                for j in range(n - i - 1, -1, -1):
                    curr_sum = (curr_sum + dp[j + 1]) % MOD
                    new_dp[j] = curr_sum
            dp = new_dp
            
        return dp[0]