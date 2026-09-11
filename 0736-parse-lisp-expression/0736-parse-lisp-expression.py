class Solution:
    def evaluate(self, expression: str) -> int:
        def parse(expr: str) -> list:
            tokens = []
            i = 0
            n = len(expr)
            while i < n:
                if expr[i] == '(' or expr[i] == ')' or expr[i] == ' ':
                    if expr[i] != ' ':
                        tokens.append(expr[i])
                    i += 1
                else:
                    j = i
                    while j < n and expr[j] not in ('(', ')', ' '):
                        j += 1
                    tokens.append(expr[i:j])
                    i = j
            return tokens

        tokens = parse(expression)
        idx = 0

        def helper(scope: dict) -> int:
            nonlocal idx
            token = tokens[idx]

            if token == '(':
                idx += 1
                op = tokens[idx]
                idx += 1

                if op == 'add':
                    val1 = helper(scope)
                    val2 = helper(scope)
                    idx += 1
                    return val1 + val2
                elif op == 'mult':
                    val1 = helper(scope)
                    val2 = helper(scope)
                    idx += 1
                    return val1 * val2
                elif op == 'let':
                    new_scope = scope.copy()
                    while True:
                        if tokens[idx] == '(':
                            res = helper(new_scope)
                            idx += 1
                            return res
                        var_or_expr = tokens[idx]
                        if tokens[idx + 1] == ')':
                            res = new_scope.get(var_or_expr, int(var_or_expr) if var_or_expr.lstrip('-').isdigit() else 0)
                            idx += 2
                            return res
                        idx += 1
                        val = helper(new_scope)
                        new_scope[var_or_expr] = val
            else:
                idx += 1
                if token.lstrip('-').isdigit():
                    return int(token)
                return scope[token]

        return helper({})