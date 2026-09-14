class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        n = len(s) // 2
        a, b = s[:n], s[n:]
        
        return sum(1 for ch in a if ch in vowels) == sum(1 for ch in b if ch in vowels)