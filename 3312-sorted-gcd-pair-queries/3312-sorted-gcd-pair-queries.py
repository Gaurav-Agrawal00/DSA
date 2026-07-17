# class Solution:

#     def findGcd(self,a,b):
#         while b != 0 :
#             a,b = b,a%b
#         return a

#     def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
#         gcdPairs = []
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 gcdPairs.append(self.findGcd(nums[i],nums[j]))
        
#         gcdPairs.sort()

#         for i in range(len(queries)):
#             queries[i] = gcdPairs[queries[i]]

#         return queries
from bisect import bisect_right
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Step 1: Har number ki frequency gin lo
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
            
        # count_gcd[g] store karega ki exact GCD 'g' wale kitne pairs hain
        count_gcd = [0] * (max_val + 1)
        
        # Step 2: Reverse loop (max_val se 1 tak) exact GCD count karne ke liye
        for g in range(max_val, 0, -1):
            # 'g' ke saare multiples ginno (g, 2g, 3g...)
            multiples = 0
            for m in range(g, max_val + 1, g):
                multiples += freq[m]
                
            # Multiples se banne wale total pairs
            pairs = multiples * (multiples - 1) // 2
            
            # Jo pairs pehle hi bade GCD (2g, 3g...) mein gine gaye hain unhe minus karo
            for m in range(2 * g, max_val + 1, g):
                pairs -= count_gcd[m]
                
            count_gcd[g] = pairs
            
        # Step 3: Prefix Sum array banao taaki pata chale kis index par kaunsa GCD hai
        prefix = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i - 1] + count_gcd[i]
            
        # Step 4: Binary search (bisect_right) se har query ka 0(1)/O(log M) mein answer do
        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(idx)
            
        return ans