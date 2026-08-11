class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=0
        p=0
        for num in nums:
            if num<0:
                c+=1
            elif num>0:
                p+=1

        return max(c,p)