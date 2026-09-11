from collections import defaultdict

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: list[str], evalints: list[int]) -> list[str]:
        eval_map = dict(zip(evalvars, evalints))

        class Poly(defaultdict):
            def __init__(self):
                super().__init__(int)

            def __add__(self, other):
                res = Poly()
                for k, v in self.items():
                    res[k] += v
                for k, v in other.items():
                    res[k] += v
                return res

            def __sub__(self, other):
                res = Poly()
                for k, v in self.items():
                    res[k] += v
                for k, v in other.items():
                    res[k] -= v
                return res

            def __mul__(self, other):
                res = Poly()
                for k1, v1 in self.items():
                    for k2, v2 in other.items():
                        new_key = tuple(sorted(k1 + k2))
                        res[new_key] += v1 * v2
                return res

        def parse(expr: str) -> list:
            tokens = []
            i = 0
            n = len(expr)
            while i < n:
                if expr[i] == ' ':
                    i += 1
                elif expr[i] in '()+-*':
                    tokens.append(expr[i])
                    i += 1
                elif expr[i].isalnum():
                    j = i
                    while j < n and expr[j].isalnum():
                        j += 1
                    tokens.append(expr[i:j])
                    i = j
            return tokens

        def make_poly(token: str) -> Poly:
            p = Poly()
            if token.isdigit():
                p[()] = int(token)
            elif token in eval_map:
                p[()] = eval_map[token]
            else:
                p[(token,)] = 1
            return p

        tokens = parse(expression)
        
        def evaluate(toks: list) -> Poly:
            polys = []
            ops = []

            def apply_op():
                op = ops.pop()
                right = polys.pop()
                left = polys.pop()
                if op == '+':
                    polys.append(left + right)
                elif op == '-':
                    polys.append(left - right)
                elif op == '*':
                    polys.append(left * right)

            i = 0
            while i < len(toks):
                t = toks[i]
                if t == '(':
                    bal = 1
                    j = i + 1
                    while j < len(toks):
                        if toks[j] == '(':
                            bal += 1
                        elif toks[j] == ')':
                            bal -= 1
                        if bal == 0:
                            break
                        j += 1
                    polys.append(evaluate(toks[i + 1:j]))
                    i = j
                elif t in ('+', '-', '*'):
                    prec = {'+': 1, '-': 1, '*': 2}
                    while ops and ops[-1] != '(' and prec.get(ops[-1], 0) >= prec[t]:
                        apply_op()
                    ops.append(t)
                else:
                    polys.append(make_poly(t))
                i += 1

            while ops:
                apply_op()

            return polys[0]

        res_poly = evaluate(tokens)
        terms = []

        for k, v in res_poly.items():
            if v != 0:
                terms.append((k, v))

        def sort_key(term):
            vars_tuple, _ = term
            return (-len(vars_tuple), vars_tuple)

        terms.sort(key=sort_key)

        ans = []
        for vars_tuple, coef in terms:
            if not vars_tuple:
                ans.append(str(coef))
            else:
                ans.append(f"{coef}*" + "*".join(vars_tuple))

        return ans