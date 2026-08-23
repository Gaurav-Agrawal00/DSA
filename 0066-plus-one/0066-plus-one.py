class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        arr = digits
        if digits[n-1] < 9:
            arr[n-1] = digits[n-1] + 1
            return arr
        
        else:
            arr.reverse()
            ans = []
            rem = 0
            left = 1
            for val in arr:
                rem = (val + left) % 10 
                ans.append(rem)
                left = (val + left) // 10
            if left > 0: 
                ans.append(left)
            ans.reverse()
            return ans