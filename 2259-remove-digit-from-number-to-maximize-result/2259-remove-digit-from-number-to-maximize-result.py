class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        
        for i in range(n - 1):
            if number[i] == digit and number[i + 1] > digit:
                return number[:i] + number[i + 1:]
                
        last_idx = number.rfind(digit)
        return number[:last_idx] + number[last_idx + 1:]

