class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for char in expression:
            if char == ',':
                continue
            if char != ')':
                stack.append(char)
            else:
                seen = set()
                while stack[-1] != '(':
                    seen.add(stack.pop())
                stack.pop()
                op = stack.pop()
                
                if op == '!':
                    stack.append('f' if 't' in seen else 't')
                elif op == '&':
                    stack.append('f' if 'f' in seen else 't')
                elif op == '|':
                    stack.append('t' if 't' in seen else 'f')
                    
        return stack[0] == 't'