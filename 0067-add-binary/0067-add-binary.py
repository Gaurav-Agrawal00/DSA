class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        left = 0
        rem = 0
        i = len(a)-1
        j = len(b)-1
        while i >= 0 or j >= 0:
            total_sum = rem
            if i >= 0:
                total_sum += int(a[i])
                i-= 1
            if j >= 0:
                total_sum += int(b[j])
                j -= 1
            ans.append(str(total_sum%2))
            rem = total_sum // 2
        if rem > 0 :
            ans.append(str(rem))
        return ''.join(ans[::-1])
