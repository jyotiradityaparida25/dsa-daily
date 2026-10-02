class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n = str(num)
        count = 0
        
        for i in range(len(n) - k + 1):
            t = int(n[i:i + k])
            if t != 0 and num % t == 0:
                count += 1
                
        return count
        