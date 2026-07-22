class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        nums.sort()
        l=[]
        for i in range(1,len(nums)):
            d=nums[i]-nums[i-1]
            l.append(d)
        l.sort()
        return l[len(l)-1]
        