class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low = i
            mid = i+1
            high = n-1
            while(mid < high):
                a = nums[low]
                b = nums[mid]
                c = nums[high]
                total = a + b + c
                if total == 0:
                    ans.append([a,b,c])
                    mid = mid + 1
                    high = high - 1

                    while mid < high and nums[mid] == nums[mid - 1]:
                        mid += 1
                        
                    while mid < high and nums[high] == nums[high + 1]:
                        high -= 1

                elif total > 0:
                    high = high-1
                else:
                    mid = mid + 1
        return [i for i in ans]