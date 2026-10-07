class Solution:
    def longestAwesome(self, s: str) -> int:
        mask_to_idx = {0: -1}
        mask = 0
        ans = 0
        
        for i, ch in enumerate(s):
            mask ^= (1 << int(ch))
            
            if mask in mask_to_idx:
                ans = max(ans, i - mask_to_idx[mask])
            else:
                mask_to_idx[mask] = i
                
            for d in range(10):
                target_mask = mask ^ (1 << d)
                if target_mask in mask_to_idx:
                    ans = max(ans, i - mask_to_idx[target_mask])
                    
        return ans