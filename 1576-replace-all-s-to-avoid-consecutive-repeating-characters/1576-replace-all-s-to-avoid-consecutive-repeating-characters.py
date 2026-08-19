class Solution:
    def modifyString(self, s: str) -> str:
        l = ['a', 'b', 'c']  
        l1 = list(s)
        n = len(l1)
        
        for i in range(n):
            if l1[i] == '?':  
                for ch in l:
                    left_ok = (i == 0 or l1[i - 1] != ch)
                    right_ok = (i == n - 1 or l1[i + 1] != ch)
                    
                    if left_ok and right_ok:
                        l1[i] = ch
                        break
                        
        return "".join(l1)
