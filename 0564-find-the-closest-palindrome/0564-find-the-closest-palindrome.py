class Solution:
    def nearestPalindromic(self, n: str) -> str:
        L = len(n)
        candidates = set()
        candidates.add(str(10**(L - 1) - 1))
        candidates.add(str(10**L + 1))
        
        prefix = int(n[:(L + 1) // 2])
        
        for p in [prefix - 1, prefix, prefix + 1]:
            p_str = str(p)
            if L % 2 == 0:
                cand = p_str + p_str[::-1]
            else:
                cand = p_str + p_str[:-1][::-1]
            candidates.add(cand)
            
        candidates.discard(n)
        
        best = ""
        min_diff = float('inf')
        n_int = int(n)
        
        for cand in candidates:
            cand_int = int(cand)
            diff = abs(cand_int - n_int)
            
            if diff < min_diff:
                min_diff = diff
                best = cand
            elif diff == min_diff:
                if cand_int < int(best):
                    best = cand
                    
        return best