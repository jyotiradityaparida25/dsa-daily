class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        l=[]
        for i in range(1,len(nums)):
            l.append(sum(nums[:i]))
        l.append(sum(nums))
        return l