class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z=bin(x^y)
        s=str(z)
        return s.count(str(1))