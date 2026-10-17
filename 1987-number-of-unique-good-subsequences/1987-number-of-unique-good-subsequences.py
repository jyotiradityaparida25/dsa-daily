class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7
        ends_with_0 = 0
        ends_with_1 = 0
        has_zero = 0
        
        for char in binary:
            if char == '1':
                ends_with_1 = (ends_with_0 + ends_with_1 + 1) % MOD
            else:
                ends_with_0 = (ends_with_0 + ends_with_1) % MOD
                has_zero = 1
                
        return (ends_with_0 + ends_with_1 + has_zero) % MOD
        