class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid=(len(nums)+1)//2
        sh=nums[:mid][::-1]
        lh=nums[mid:][::-1]
        nums[0::2]=sh
        nums[1::2]=lh