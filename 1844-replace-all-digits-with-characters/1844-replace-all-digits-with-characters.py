class Solution:
    def replaceDigits(self, s: str) -> str:
        l=[c for c in s]
        for i in range(1,len(l)):
            if l[i].isdigit():
                l[i]=chr(ord(l[i-1])+int(l[i]))
        
        return "".join(l)