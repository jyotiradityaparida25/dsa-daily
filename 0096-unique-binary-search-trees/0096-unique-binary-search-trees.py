class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=[0]*(n+1)
        b[0]=1
        b[1]=1
        for i in range(2,n+1):
            for j in range(1,i+1):
                l=j-1
                r=i-j
                b[i]+=b[l]*b[r]
        return b[n]
        