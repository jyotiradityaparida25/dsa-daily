class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""
        for d in "9876543210":
            candidate = d * 3
            if candidate in num:
                return candidate
        return best