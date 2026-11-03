class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        max_val = max(nums)
        for num in nums:
            moves += max_val - num
        return moves