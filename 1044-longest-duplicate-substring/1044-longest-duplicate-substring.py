class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        mod = (1 << 61) - 1

        def search(length: int) -> int:
            base = 26
            h = 0
            for i in range(length):
                h = (h * base + nums[i]) % mod

            seen = {h}
            aL = pow(base, length, mod)

            for i in range(1, n - length + 1):
                h = (h * base - nums[i - 1] * aL + nums[i + length - 1]) % mod
                if h in seen:
                    return i
                seen.add(h)
            return -1

        low, high = 1, n - 1
        start = -1
        max_len = 0

        while low <= high:
            mid = (low + high) // 2
            idx = search(mid)
            if idx != -1:
                low = mid + 1
                start = idx
                max_len = mid
            else:
                high = mid - 1

        return s[start:start + max_len] if start != -1 else ""