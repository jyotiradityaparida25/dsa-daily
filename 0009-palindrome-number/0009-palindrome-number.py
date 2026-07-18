class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        if x<0:
            return False
        return s==s[::-1]
        