class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        l = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if cnt > 0:
                    stack.append(s[l : l + cnt])
                    cnt = 0
                l = i + 1
                continue
            else:
                cnt += 1
        if cnt > 0:
            stack.append(s[l : l + cnt])
        stack.reverse()
        return " ".join(stack)