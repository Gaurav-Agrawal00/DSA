
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for val in asteroids:
            if val < 0 :
                if stack and stack[-1] > 0:
                    while stack and stack[-1] > 0 and stack[-1] < abs(val) :
                        stack.pop()
                    if stack and stack[-1] == abs(val) :
                        stack.pop()
                        continue
                    if len(stack) == 0 or stack[-1] < 0:
                        stack.append(val)
                else:
                    stack.append(val)
            else:
                stack.append(val)
        return stack