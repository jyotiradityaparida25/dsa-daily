class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        l = []
        for i in range(len(nums)):
            if nums[i] == 1:
                for j in range(i + 1, len(nums)):
                    if nums[j] == 2:
                        l.append(j - i)
            elif nums[i] == 2:
                for j in range(i + 1, len(nums)):
                    if nums[j] == 1:
                        l.append(j - i)
        return min(l) if l else -1