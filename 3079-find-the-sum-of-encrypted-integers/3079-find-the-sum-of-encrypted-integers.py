class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        l1=[]
        def encrypt(x):
            if len(str(x))==1:
                return x
            l=[]
            while x>0:
                d=x%10
                x=x//10
                l.append(d)
            l.sort()
            return l[-1]
        for num in nums:
            c=encrypt(num)
            res=""
            for i in range(len(str(num))):
                res+=str(c)
            l1.append(int(res))
        return sum(l1)