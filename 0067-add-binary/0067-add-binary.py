class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def binaryCalculate(s):
            sum=0
            for i in range(len(s)):
                if s[i]=='1':
                    sum+=2**(len(s)-1-i)
            return sum
        total=binaryCalculate(a)+binaryCalculate(b)
        return str(format(total,'b'))

        