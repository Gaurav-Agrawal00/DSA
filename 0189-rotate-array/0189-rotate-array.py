class Solution:

    def reverseArr(self,start,end,nums):
        while start <= end-1 :
            nums[start],nums[end-1] = nums[end-1],nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverseArr(0,n-k,nums)
        self.reverseArr(n-k,n,nums)
        self.reverseArr(0,n,nums)
        return nums