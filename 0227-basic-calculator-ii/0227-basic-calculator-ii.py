class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        operator = '+'  
        
        for i, char in enumerate(s):
           
            if char.isdigit():
                current_num = current_num * 10 + int(char)
                
            if char in "+-*/" or i == len(s) - 1:
                if operator == '+':
                    stack.append(current_num)
                elif operator == '-':
                    stack.append(-current_num)
                elif operator == '*':
                    stack.append(stack.pop() * current_num)
                elif operator == '/':
                   
                    stack.append(int(stack.pop() / current_num))
           
                operator = char
                current_num = 0
 
        return sum(stack)