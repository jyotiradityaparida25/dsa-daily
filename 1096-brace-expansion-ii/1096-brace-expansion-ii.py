import itertools

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(expr: str) -> set[str]:
            res = set()
            groups = []
            curr_group = [set([""])]
            i = 0
            n = len(expr)
            
            while i < n:
                if expr[i] == '{':
                    j = i
                    balance = 0
                    while j < n:
                        if expr[j] == '{':
                            balance += 1
                        elif expr[j] == '}':
                            balance -= 1
                            if balance == 0:
                                break
                        j += 1
                    
                    sub_res = parse(expr[i + 1:j])
                    curr_group.append(sub_res)
                    i = j + 1
                elif expr[i] == ',':
                    product = set(
                        "".join(parts)
                        for parts in itertools.product(*curr_group)
                    )
                    res.update(product)
                    curr_group = [set([""])]
                    i += 1
                else:
                    curr_group.append({expr[i]})
                    i += 1
            
            product = set(
                "".join(parts)
                for parts in itertools.product(*curr_group)
            )
            res.update(product)
            return res

        return sorted(list(parse(expression)))