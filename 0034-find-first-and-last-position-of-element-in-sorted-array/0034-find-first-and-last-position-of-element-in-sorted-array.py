class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFirst(nums,target):
            l=0
            r=len(nums)-1
            res=-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    res=m
                    r=m-1
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return res
        def findLast(nums,target):
            l,r=0,len(nums)-1
            res=-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    res=m
                    l=m+1
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return res
        return (findFirst(nums,target),findLast(nums,target))
