class Solution:
    def totalMoney(self, n: int) -> int:
        n1=n//7
        n2=n%7
        a=1
        b=0
        s=0
        while n1>0:
            b=a
            for i in range(7):
                s+=b
                b+=1
            n1-=1
            a+=1
        for i in range(n2):
            s+=a
            a+=1
        return s
