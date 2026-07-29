class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
            
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            if n == 0:
                return []
            if n < 20:
                return [less_than_20[n]]
            if n < 100:
                return [tens[n // 10]] + helper(n % 10)
            return [less_than_20[n // 100], "Hundred"] + helper(n % 100)
            
        res = []
        for i in range(4):
            if num % 1000 != 0:
                res = helper(num % 1000) + ([thousands[i]] if thousands[i] else []) + res
            num //= 1000
            
        return " ".join(res)