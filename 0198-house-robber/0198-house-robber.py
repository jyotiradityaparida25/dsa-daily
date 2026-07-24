class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=0
        for m in nums:
            c=max(m+a,b)
            a=b
            b=c
        return b
        