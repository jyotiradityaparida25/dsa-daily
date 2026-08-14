class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a1=text.count('b')
        a2=text.count('a')
        a3=text.count('l')//2
        a4=text.count('o')//2
        a5=text.count('n')
        return min(a1,a2,a3,a4,a5)