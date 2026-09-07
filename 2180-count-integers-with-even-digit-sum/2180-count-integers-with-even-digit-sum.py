class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            s=sum(int(c) for c in str(i))
            if s%2==0:
                c+=1
        
        return c