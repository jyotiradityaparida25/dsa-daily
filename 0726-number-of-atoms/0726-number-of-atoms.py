class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i, n = 0, len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i]) if start < i else 1
                for elem, count in top.items():
                    stack[-1][elem] += count * mult
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i]) if start < i else 1
                stack[-1][elem] += count
                
        res = []
        for elem in sorted(stack[-1].keys()):
            count = stack[-1][elem]
            res.append(elem + (str(count) if count > 1 else ""))
            
        return "".join(res)