class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        unique_nums = set()
        res = ""
        
        for ch in word:
            if ch.isdigit():
                res += ch
            else:
                if res:
                    unique_nums.add(int(res))
                    res = ""
                    
        if res:
            unique_nums.add(int(res))
            
        return len(unique_nums)
