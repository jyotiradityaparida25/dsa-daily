class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res=''
        for i in s:
            res+=(str(ord(i)-ord('a')+1))

        s=0

        for _ in range(k):
            res=str(sum(int(d) for d in res))

        return int(res)