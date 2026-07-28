class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask_to_len = {}
        
        for word in words:
            mask = 0
  
            for char in word:
              
                mask |= 1 << (ord(char) - ord('a'))
            
            mask_to_len[mask] = max(mask_to_len.get(mask, 0), len(word))
            
        max_product = 0
        
        for mask1, len1 in mask_to_len.items():
            for mask2, len2 in mask_to_len.items():
                
                if mask1 & mask2 == 0:
                    max_product = max(max_product, len1 * len2)
                    
        return max_product