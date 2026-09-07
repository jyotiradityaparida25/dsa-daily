class Solution:
    def digitCount(self, num: str) -> bool:
        t=[int(c) for c in num]
        for i in range(len(num)):
            if int(num[i])!=t.count(i):
                return False
        return True
