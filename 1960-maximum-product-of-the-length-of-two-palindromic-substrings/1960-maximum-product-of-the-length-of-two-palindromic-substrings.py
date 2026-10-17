class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        
        radius = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(radius[l + r - i], r - i + 1)
            while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                k += 1
            radius[i] = k - 1
            if i + radius[i] > r:
                l = i - radius[i]
                r = i + radius[i]

        left_max = [1] * n
        right_max = [1] * n

        curr = 1
        for i in range(n):
            curr = max(curr, radius[i] * 2 + 1)
            left_max[i] = curr
            
        curr = 1
        for i in range(n - 1, -1, -1):
            curr = max(curr, radius[i] * 2 + 1)
            right_max[i] = curr

        l_idx = 0
        for i in range(n):
            while l_idx + radius[l_idx] < i:
                l_idx += 1
            left_max[i] = max(left_max[i - 1] if i > 0 else 1, (i - l_idx) * 2 + 1)

        r_idx = n - 1
        for i in range(n - 1, -1, -1):
            while r_idx - radius[r_idx] > i:
                r_idx -= 1
            right_max[i] = max(right_max[i + 1] if i + 1 < n else 1, (r_idx - i) * 2 + 1)

        ans = 1
        for i in range(n - 1):
            ans = max(ans, left_max[i] * right_max[i + 1])

        return ans