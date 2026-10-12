class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % MOD
            
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

        counts = [0] * 26
        ans = 0
        
        for i in range(n - 1, -1, -1):
            digit = ord(s[i]) - ord('a')
            counts[digit] += 1
            
            smaller_count = sum(counts[:digit])
            
            if smaller_count > 0:
                length = n - 1 - i
                permutations = (fact[length] * smaller_count) % MOD
                for c in counts:
                    if c > 1:
                        permutations = (permutations * inv_fact[c]) % MOD
                ans = (ans + permutations) % MOD
                
        return ans