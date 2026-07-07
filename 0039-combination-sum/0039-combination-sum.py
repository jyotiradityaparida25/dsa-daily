class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def backtrack(s,r,p):
            if r==0:
                res.append(p[:])
                return
            if r<0:
                return
            for i in range(s,len(candidates)):
                p.append(candidates[i])
                backtrack(i,r-candidates[i],p)
                p.pop()
        backtrack(0,target,[])
        return res
        