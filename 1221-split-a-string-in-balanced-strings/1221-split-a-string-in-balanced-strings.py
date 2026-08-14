class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        splits = 0
        
        for char in s:
            
            if char == 'L':
                balance += 1
            else:
                balance -= 1
                
            if balance == 0:
                splits += 1
                
        return splits