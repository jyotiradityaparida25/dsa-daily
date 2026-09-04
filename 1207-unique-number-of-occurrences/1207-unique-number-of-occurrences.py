class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l=[]
        a=set(arr)
        for num in a:
            if arr.count(num) in l:
                return False
            else:
                l.append(arr.count(num))
        return True