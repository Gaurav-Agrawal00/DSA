class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # cntE = 0
        # cntZ = 0
        # for digit in digits:
        #     if digit % 2 == 0:
        #         cntE += 1
        #         if digit == 0:
        #             cntZ += 1
        map_freq = {}
        for digit in digits:
            map_freq[digit] = map_freq.get(digit,0) + 1
        
        ans = 0
        for i in range(100,1000,2):
            n = i
            isValid = True
            temp = map_freq.copy()
            while n:
                val = n % 10
                if temp.get(val , 0) == 0:
                    isValid = False
                    break
                else:
                    temp[val] -= 1
                n = n // 10
            if isValid:
                ans += 1
        return ans