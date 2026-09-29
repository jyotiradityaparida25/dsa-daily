class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 0
        last = {}
        
        for char in s:
            new_subseqs = (dp + 1) % MOD
            dp = (dp + new_subseqs - last.get(char, 0)) % MOD
            last[char] = new_subseqs
            
        return dp