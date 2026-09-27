class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(2,1000,2):
            if i%2==0 and i%n==0:
                return i
                break
        
        return -1