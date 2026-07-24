class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s=set(nums)
        if len(nums)!=len(s):
            return True
        return False
        