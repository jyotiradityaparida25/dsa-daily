class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s:
            return True
        if 'ba' in s:
            return False
        return True
