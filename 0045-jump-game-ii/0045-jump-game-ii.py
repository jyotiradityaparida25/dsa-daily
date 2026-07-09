class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=1:
            return 0
        j=0
        curr=0
        far=0
        for i in range(n-1):
            far=max(far,i+nums[i])
            if i==curr:
                j+=1
                curr=far
                if curr>=n-1:
                    break
        return j