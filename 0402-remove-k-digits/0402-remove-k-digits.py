class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return '0'
        stack = []
        i = 0
        while i < n :
            while stack and stack[-1] > num[i] and k != 0:
                k -= 1
                stack.pop()
            stack.append(num[i])
            i += 1
            if k == 0:
                break
            
        while i < n:
            stack.append(num[i])
            i += 1
        
        while k > 0 :
            stack.pop()
            k-=1
        
        # stack.reverse()
        ans = ''.join(stack)
        ans = ans.lstrip('0')
        return ans if ans else '0'