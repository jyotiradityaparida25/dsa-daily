class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        p1=[]
        p2=[]
        p1.append(nums[0])
        p2.append(nums[1])
        for i in range(2,len(nums)):
            if p1[len(p1)-1]>p2[len(p2)-1]:
                p1.append(nums[i])
            else:
                p2.append(nums[i])
        return p1+p2