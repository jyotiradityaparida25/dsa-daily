class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[j]<nums[i]:
                    c+=1
            l.append(c)
            c=0
        return l
                