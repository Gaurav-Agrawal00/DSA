class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(' , '[' , '{'}
        hash_map = {'(' : ')' , '[' : ']' , '{': '}'}
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if len(stack) == 0 or hash_map[stack[-1]] != s[i]:
                    return False
                
                stack.pop()
        if stack:
            return False
        return True