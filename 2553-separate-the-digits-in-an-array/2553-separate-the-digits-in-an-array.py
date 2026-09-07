class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        for num in nums:
            c=str(num)
            for i in range(len(c)):
                l.append(int(c[i]))
        return l