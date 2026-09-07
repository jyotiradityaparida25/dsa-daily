class Solution:
    def minElement(self, nums: List[int]) -> int:
        l=[]
        for num in nums:
            temp=sum(int(d) for d in str(num))
            l.append(temp)
        l.sort()
        return l[0]