class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        def backtrack(s,r,p):
            if r==0:
                res.append(p[:])
                return
            if r<0:
                return
            for i in range(s,len(candidates)):
                if candidates[i]>r:
                    break
                if i>s and candidates[i]==candidates[i-1]:
                    continue
                p.append(candidates[i])
                backtrack(i+1,r-candidates[i],p)
                p.pop()
        backtrack(0,target,[])
        return res
        