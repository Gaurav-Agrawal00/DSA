class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n-2):
            low = i
            mid = i+1
            high = n-1
            while(mid < high):
                a = nums[low]
                b = nums[mid]
                c = nums[high]
                total = a + b + c
                if total == 0:
                    ans.add(tuple([a,b,c]))
                    mid = mid + 1
                elif total > 0:
                    high = high-1
                else:
                    mid = mid + 1
        return [i for i in ans]