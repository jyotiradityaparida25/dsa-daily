class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        pairs = 0
        leftovers = 0
        
        for count in counts.values():
            pairs += count // 2
            leftovers += count % 2
            
        return [pairs, leftovers]