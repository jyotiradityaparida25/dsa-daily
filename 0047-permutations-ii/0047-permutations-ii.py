import itertools
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        obj=itertools.permutations(nums)
        s=set(obj)
        return list(s)