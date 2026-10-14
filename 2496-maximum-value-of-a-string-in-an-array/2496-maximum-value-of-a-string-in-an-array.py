class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        mx=-1
        t=0
        for s in strs:
            if s.isnumeric():
                t=int(s)
                mx=max(mx,t)
            else:
                t=len(s)
                mx=max(mx,t)
        return mx