class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
            
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        
        lps = [0] * len(combined)
        j = 0
        
        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            
            if combined[i] == combined[j]:
                j += 1
                
            lps[i] = j
            
        palindromic_prefix_len = lps[-1]
        
        suffix_to_add = rev_s[:len(s) - palindromic_prefix_len]
        
        return suffix_to_add + s  