class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(p1, p2):
            if p1 is None:
                return 0
            r1, c1 = divmod(p1, 6)
            r2, c2 = divmod(p2, 6)
            return abs(r1 - r2) + abs(c1 - c2)
        
        memo = {}
        
        def dp(i, other):
            if i == len(word):
                return 0
            
            state = (i, other)
            if state in memo:
                return memo[state]
            
            curr = ord(word[i]) - ord('A')
            prev = ord(word[i - 1]) - ord('A') if i > 0 else None
            
            cost1 = dist(prev, curr) + dp(i + 1, other)
            
            cost2 = dist(other, curr) + dp(i + 1, prev)
            
            memo[state] = min(cost1, cost2)
            return memo[state]
            
        return dp(0, None)