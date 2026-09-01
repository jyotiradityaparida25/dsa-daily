class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        s=nums[0]
        l=nums[len(nums)-1]
        l1=[i for i in range(s,l+1)]
        l2=[]
        for i in l1:
            if i not in nums:
                l2.append(i)
        return l2
                