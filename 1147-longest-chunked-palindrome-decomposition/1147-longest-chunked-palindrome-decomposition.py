class Solution:
    def longestDecomposition(self, text: str) -> int:
        l, r = 0, len(text) - 1
        left_sub, right_sub = "", ""
        ans = 0

        while l < r:
            left_sub += text[l]
            right_sub = text[r] + right_sub

            if left_sub == right_sub:
                ans += 2
                left_sub, right_sub = "", ""

            l += 1
            r -= 1

        if l == r or left_sub:
            ans += 1

        return ans