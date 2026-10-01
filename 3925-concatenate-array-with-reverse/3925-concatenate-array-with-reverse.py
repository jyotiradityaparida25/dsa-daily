class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        l=[]
        for i in range(len(nums)):
            l.append(nums[i])
        for j in range(len(nums)-1,-1,-1):
            l.append(nums[j])

        return l