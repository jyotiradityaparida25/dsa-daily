from fractions import Fraction

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert(num_str: str) -> Fraction:
            if '.' not in num_str:
                return Fraction(int(num_str), 1)
            
            dot_idx = num_str.index('.')
            integer_part = num_str[:dot_idx]
            
            if '(' not in num_str:
                non_repeating = num_str[dot_idx + 1:]
                if not non_repeating:
                    return Fraction(int(integer_part), 1)
                return Fraction(int(integer_part + non_repeating), 10 ** len(non_repeating))
            
            paren_idx = num_str.index('(')
            non_repeating = num_str[dot_idx + 1:paren_idx]
            repeating = num_str[paren_idx + 1:-1]
            
            val_fixed = Fraction(int(integer_part + non_repeating), 10 ** len(non_repeating)) if (integer_part + non_repeating) else Fraction(0)
            val_rep = Fraction(int(repeating), (10 ** len(repeating) - 1) * (10 ** len(non_repeating)))
            
            return val_fixed + val_rep

        return convert(s) == convert(t)