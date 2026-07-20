class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for val in s:
            if val == "]" or val == "}" or val == ")":
                if len(stack) == 0:
                    return False
                if (
                    (val == ")" and stack[-1] != "(")
                    or (val == "]" and stack[-1] != "[")
                    or (val == "}" and stack[-1] != "{")
                ):
                    return False
                else:
                    stack.pop()

            else:
                stack.append(val)
        return len(stack) == 0
