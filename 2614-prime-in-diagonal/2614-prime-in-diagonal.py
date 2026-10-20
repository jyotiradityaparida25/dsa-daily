class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(n):
            if n<2:
                return False
            for i in range(2,int(0.5*n)+1):
                if n%i==0:
                    return False
            return True
        mx=0
        n=len(nums)
        for i in range(len(nums)):
            for j in (nums[i][i] ,nums[i][n-i-1]):
                if j>mx and isPrime(j):
                    mx=j
        return mx
