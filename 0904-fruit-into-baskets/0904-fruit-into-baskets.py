class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        maxLen = 0
        ansSet = {}
        while r < len(fruits):
            ansSet[fruits[r]] = ansSet.get(fruits[r],0) + 1
            if len(ansSet) > 2 :
                ansSet[fruits[l]] -= 1
                if ansSet[fruits[l]] == 0:
                    del ansSet[fruits[l]]
                l += 1
            maxLen = max(maxLen,r-l+1)
            r += 1
        return maxLen