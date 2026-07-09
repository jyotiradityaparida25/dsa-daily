class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        m=mat
        n=len(m)
        for _ in range(4):
            if m==target:
                return True
            
            for i in range(n):
                for j in range(i+1,n):
                    m[i][j],m[j][i]=m[j][i],m[i][j]
        
            for r in m:
                r.reverse()
        return False
        
        