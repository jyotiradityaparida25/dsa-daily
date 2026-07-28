class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k=len(primes)
        p=[0]*k
        u=[0]*n
        u[0]=1
        nm=primes[:]
        for i in range(1,n):
            nu=min(nm)
            u[i]=nu
            for j in range(k):
                if nm[j]==nu:
                    p[j]+=1
                    nm[j]=u[p[j]]*primes[j]
        return u[-1]