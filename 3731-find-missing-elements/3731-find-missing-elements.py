class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        big = max(nums)
        num_set = set(nums)
        ans = []
        for i in range(small,big+1):
            if i not in num_set:
                ans.append(i)
        return ans