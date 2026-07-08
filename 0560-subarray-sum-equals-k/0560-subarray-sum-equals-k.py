class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_set ={0:1}
        cnt = 0
        sum1 = 0
        for num in nums:
            sum1 += num
            target = sum1 - k
            if  target in hash_set:
                cnt += hash_set[target]
            
            hash_set[sum1] = hash_set.get(sum1,0) + 1

        return cnt