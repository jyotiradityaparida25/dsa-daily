class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def check(ch):
            l=[c for c in ch]
            if ord(l[0])%2!=0 and ord(l[1])%2!=0:
                return False
            elif ord(l[0])%2==0 and ord(l[1])%2==0:
                return False
            else:
                return True

        return check(coordinate1)==check(coordinate2)