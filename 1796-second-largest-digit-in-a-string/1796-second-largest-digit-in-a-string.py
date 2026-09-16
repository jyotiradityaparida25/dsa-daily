class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1
        
        for char in s:
            if char.isdigit():
                val = int(char)
                if val > first:
                    second = first
                    first = val
                elif first > val > second:
                    second = val
                    
        return second