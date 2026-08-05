class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = len(num1) - 1
        b = len(num2) - 1
        carry = 0
        res = []
        
        while a >= 0 or b >= 0 or carry:
            val1 = int(num1[a]) if a >= 0 else 0
            val2 = int(num2[b]) if b >= 0 else 0
            
            total = val1 + val2 + carry
            res.append(str(total % 10))
            carry = total // 10
            
            a -= 1
            b -= 1
            
        return "".join(res[::-1])
        