class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        s = str(n)
        k = len(s)
        num_digits = len(digits)
        ans = 0

        for i in range(1, k):
            ans += num_digits ** i

        for i, char in enumerate(s):
            has_same_digit = False

            for d in digits:
                if d < char:
                  
                    ans += num_digits ** (k - i - 1)
                elif d == char:
                    
                    has_same_digit = True
                    break
                else:
                    
                    break

            if not has_same_digit:
                return ans

        return ans + 1