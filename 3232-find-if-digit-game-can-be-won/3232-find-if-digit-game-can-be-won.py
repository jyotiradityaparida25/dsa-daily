class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        l=[d for d in nums if len(str(d))==1]
        l1=[d for d in nums if len(str(d))==2]
        if sum(l)==sum(l1):
            return False
        return True