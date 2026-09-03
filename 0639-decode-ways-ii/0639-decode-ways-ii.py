class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        
        def ways_single(c: str) -> int:
            if c == '*': return 9
            if c == '0': return 0
            return 1
            
        def ways_pair(c1: str, c2: str) -> int:
            if c1 == '*' and c2 == '*':
                return 15
            elif c1 == '*':
                return 2 if '0' <= c2 <= '6' else 1
            elif c2 == '*':
                if c1 == '1': return 9
                if c1 == '2': return 6
                return 0
            else:
                return 1 if 10 <= int(c1 + c2) <= 26 else 0
                
        dp0, dp1 = 1, ways_single(s[0])
        
        for i in range(1, len(s)):
            dp_next = (dp1 * ways_single(s[i]) + dp0 * ways_pair(s[i-1], s[i])) % MOD
            dp0, dp1 = dp1, dp_next
            
        return dp1