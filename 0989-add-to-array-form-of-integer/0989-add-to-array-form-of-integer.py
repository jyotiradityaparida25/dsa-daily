class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            num[i] += k
            k = num[i] // 10
            num[i] %= 10
            
        while k > 0:
            num.insert(0, k % 10)
            k //= 10
            
        return num