class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
            
        n = abs(num)
        res = []
        
        while n > 0:
            res.append(str(n % 7))
            n //= 7
            
        if num < 0:
            res.append("-")
            
        return "".join(res[::-1])
     