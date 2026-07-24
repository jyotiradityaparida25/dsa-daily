class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        numss=[str(num) for num in nums]
        numss.sort(key=lambda x:x*10 ,reverse=True)
        lgn=''.join(numss)
        if lgn[0]=='0':
            return '0'
        return lgn
        