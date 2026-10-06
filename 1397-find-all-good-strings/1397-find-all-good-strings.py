class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        m = len(evil)
        
        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and evil[i] != evil[j]:
                j = pi[j - 1]
            if evil[i] == evil[j]:
                j += 1
            pi[i] = j

        def get_next_match(match_len: int, ch: str) -> int:
            while match_len > 0 and evil[match_len] != ch:
                match_len = pi[match_len - 1]
            if evil[match_len] == ch:
                match_len += 1
            return match_len

        memo = {}

        def dp(i: int, evil_match: int, is_less: bool, is_more: bool) -> int:
            if evil_match == m:
                return 0
            if i == n:
                return 1

            state = (i, evil_match, is_less, is_more)
            if state in memo:
                return memo[state]

            start_char = 'a' if is_more else s1[i]
            end_char = 'z' if is_less else s2[i]

            total = 0
            for ch_ord in range(ord(start_char), ord(end_char) + 1):
                ch = chr(ch_ord)
                next_evil = get_next_match(evil_match, ch)
                next_is_less = is_less or (ch < s2[i])
                next_is_more = is_more or (ch > s1[i])
                
                total = (total + dp(i + 1, next_evil, next_is_less, next_is_more)) % MOD

            memo[state] = total
            return total

        return dp(0, 0, False, False)