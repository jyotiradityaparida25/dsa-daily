class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        l=[c for c in coordinates]
        if ord(l[0])%2!=0 and ord(l[1])%2!=0:
            return False
        elif ord(l[0])%2==0 and ord(l[1])%2==0:
            return False
        else:
            return True