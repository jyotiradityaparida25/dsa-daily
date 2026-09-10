class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m=-1
        for num in arr:
            if arr.count(num)==num:
                if arr.count(num)>m:
                    m=arr.count(num)
        
        return m