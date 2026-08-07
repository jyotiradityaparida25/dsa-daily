class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s1=s.split('-')
        r=''.join(s1)
        r1=r[::-1].upper()
        r2=''
        for i in range(len(r1)):
            if i%k==0 and i!=0:
                r2+='-'
                r2+=r1[i]
            else:
                r2+=r1[i]
        return r2[::-1]