class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s1=s
        while len(s1)!=2:
            res=''
            for i in range(1,len(s1)):
                t=str((int(s1[i-1])+int(s1[i]))%10)
                res+=t
            s1=res
        if int(s1[0])!=int(s1[1]):
            return False
        return True