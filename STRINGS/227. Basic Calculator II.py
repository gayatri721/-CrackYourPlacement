class Solution:
    def calculate(self, s: str) -> int:
        op, val = "+", 0 #initialized at "+0"
        stack = []
        for i, x in enumerate(s):
            if x.isdigit(): val = 10*val + int(x) #accumulating digits 
                
            if x in "+-*/" or i == len(s) - 1: #
                if   op == "+": stack.append(val)
                elif op == "-": stack.append(-val)
                elif op == "*": stack.append(stack.pop() * val)
                elif op == "/": stack.append(int(stack.pop()/val))
                op, val = x, 0 #reset 
        return sum(stack)
