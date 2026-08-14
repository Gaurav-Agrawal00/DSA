class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        a = s + s
        for i in range(len(s)):
            if goal == a[i : len(s) + i]:
                return True
        return False 