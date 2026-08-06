class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a = -1
        b = -1 
        length = 0
        maxCnt = 0
        l = 0 
        l1 = 0
        r = 0
        while r < len(fruits):
            # 1. Agar naya fruit aaya jo dono baskets mein nahi hai
            if fruits[r] != a and fruits[r] != b:
                if a < 0:
                    a = fruits[r]
                elif b < 0:
                    b = fruits[r]
                else:
                    l = l1
                    a = fruits[r-1]
                    b = fruits[r]
            
            # 2. 'l1' hamesha aakhiri continuous same fruits ke block ka index hona chahiye
            if r > 0 and fruits[r] != fruits[r-1]:
                l1 = r
                
            length = r - l + 1
            maxCnt = max(length, maxCnt)
            r += 1
        return maxCnt