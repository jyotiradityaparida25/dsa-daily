class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i]==stones[j]:
                    c+=1
        return c