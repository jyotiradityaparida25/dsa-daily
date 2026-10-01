class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in range(2):
            for j in range(len(nums)):
                ans.append(nums[j])

        return ans