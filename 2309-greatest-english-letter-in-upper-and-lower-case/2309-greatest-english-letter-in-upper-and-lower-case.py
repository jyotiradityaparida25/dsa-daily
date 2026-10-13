class Solution:
    def greatestLetter(self, s: str) -> str:
        l=[]
        l.append("")
        for le in s:
            if le.lower() in s and le.upper() in s:
                l.append(le.upper())
        l.sort()
        return l[-1]