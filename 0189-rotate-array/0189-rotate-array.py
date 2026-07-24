class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        d=len(nums)-k
        l=nums[:d]
        l1=nums[d:]
        nums[:]=l1+l
        return nums