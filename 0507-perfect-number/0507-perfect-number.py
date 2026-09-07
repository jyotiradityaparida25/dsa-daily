class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
            
        total = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                total += i + (num // i if i * i != num else 0)
                
        return total == num
        