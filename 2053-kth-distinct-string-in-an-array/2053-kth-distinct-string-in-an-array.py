class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        s=set()
        c=0
        for a in arr:
            if arr.count(a)==1:
                c+=1
                if c==k:
                    return a
        return ""