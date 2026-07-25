class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            
        diff_bit = 1
        while not (diff_bit & xor_sum):
            diff_bit = diff_bit << 1
            
        a = 0
        b = 0
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num
                
        return [a, b]