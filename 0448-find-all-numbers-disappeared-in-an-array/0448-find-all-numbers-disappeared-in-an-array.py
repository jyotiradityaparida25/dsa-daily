class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l1=set(nums)
        l2=[]
        for i in range(1,n+1):
            if i not in l1:
                l2.append(i)
        return l2