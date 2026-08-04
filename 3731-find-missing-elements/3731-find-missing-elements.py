class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        big = max(nums)
        ans_set = {}
        n = big-small+1
        for num in nums:
            ans_set[num] = True

        ans = []
        for i in range(small,big+1):
            if i not in ans_set:
                ans.append(i)
        return ans