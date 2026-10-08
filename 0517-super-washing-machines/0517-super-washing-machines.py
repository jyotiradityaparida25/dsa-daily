class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        
        target = total // n
        ans = 0
        balance = 0
        
        for count in machines:
            diff = count - target
            balance += diff
            ans = max(ans, abs(balance), diff)
            
        return ans