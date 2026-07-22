class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=[ch.lower() for ch in s if ch.isalnum()]
        return s1==s1[::-1]
        