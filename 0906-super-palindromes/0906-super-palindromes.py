class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L = int(left)
        R = int(right)
        ans = 0

        def is_palindrome(val: int) -> bool:
            s = str(val)
            return s == s[::-1]

        for k in range(1, 100000):
            s = str(k)
            
            root_odd = int(s + s[-2::-1])
            sq_odd = root_odd * root_odd
            if sq_odd > R:
                pass
            elif sq_odd >= L and is_palindrome(sq_odd):
                ans += 1
                
            root_even = int(s + s[::-1])
            sq_even = root_even * root_even
            if sq_even > R:
                pass
            elif sq_even >= L and is_palindrome(sq_even):
                ans += 1

        return ans