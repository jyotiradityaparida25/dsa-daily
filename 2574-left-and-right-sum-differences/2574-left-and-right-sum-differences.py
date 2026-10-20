class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls=[]
        rs=[]
        ls.append(0)
        a,b=0,0
        for i in range(len(nums)):
            a=sum(nums[:i+1])
            b=sum(nums[i+1:])
            ls.append(a)
            rs.append(b)

        l=[]
        r,s=0,0
        while r<len(ls) and s<len(rs):
            l.append(abs(ls[r]-rs[s]))
            r+=1
            s+=1
        return l