class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []
        
        for j, c in enumerate(s):
            count += 1 if c == '1' else -1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1
                
        res.sort(reverse=True)
        return "".join(res)