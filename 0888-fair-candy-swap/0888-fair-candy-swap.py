class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a=sum(aliceSizes)
        sum_b=sum(bobSizes)
        diff=(sum_b-sum_a)//2
        bs=set(bobSizes)
        for x in aliceSizes:
            if x+diff in bs:
                return [x,x+diff]

