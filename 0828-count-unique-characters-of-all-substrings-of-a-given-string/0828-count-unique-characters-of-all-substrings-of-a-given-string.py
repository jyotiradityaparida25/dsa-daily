class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        last_seen = {}
        left = [0] * n
        for i, ch in enumerate(s):
            left[i] = i - last_seen.get(ch, -1)
            last_seen[ch] = i

        next_seen = {}
        right = [0] * n
        for i in range(n - 1, -1, -1):
            ch = s[i]
            right[i] = next_seen.get(ch, n) - i
            next_seen[ch] = i

        return sum(left[i] * right[i] for i in range(n))