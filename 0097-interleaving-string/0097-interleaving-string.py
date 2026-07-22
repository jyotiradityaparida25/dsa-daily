class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3):
            return False
        m={}
        def dfs(i,j):
            if i==len(s1) and j==len(s2):
                return True
            if (i,j) in m:
                return m[(i,j)]
            k=i+j
            valid=False
            if i<len(s1) and s1[i]==s3[k]:
                valid =dfs(i+1,j)
            if not valid and j<len(s2) and s2[j]==s3[k]:
                valid=dfs(i,j+1)
            m[(i,j)]=valid
            return valid
        return dfs(0,0)
        