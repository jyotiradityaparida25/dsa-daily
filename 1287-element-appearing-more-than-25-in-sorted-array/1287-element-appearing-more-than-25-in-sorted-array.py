class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        mx=0.25*len(arr)
        for num in arr:
            if arr.count(num)>mx:
                return num
        return -1