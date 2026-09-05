class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        pairs = []
        
        for spell in spells:
            
            threshold = (success + spell - 1) // spell  
            idx = bisect_left(potions, threshold)
            pairs.append(m - idx)
        
        return pairs