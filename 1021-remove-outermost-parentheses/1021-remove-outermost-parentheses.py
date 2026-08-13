class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        opened = 0
        for val in s:
            if val == '(' and opened > 0:
                stack.append(val)            
            
            elif val == ')' and opened > 1:
                stack.append(val)
                
            opened += 1 if val == "(" else -1
        return "".join(stack)
