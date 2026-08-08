class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s1=s
        for _ in range(len(s)):
            lr=s1[1:]+s1[0]
            if lr==goal:
                return True
                break
            else:
                s1=lr
        return False