class Solution:
    def maxScore(self, s: str) -> int:
        ones_on_right = s.count('1')
        
        zeros_on_left = 0
        max_score = 0
        
        for i in range(len(s) - 1):
            if s[i] == '0':
                
                zeros_on_left += 1
            else:
                
                ones_on_right -= 1
                
            current_score = zeros_on_left + ones_on_right
            
            max_score = max(max_score, current_score)
            
        return max_score