class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        # Step 1: Pura array ka total XOR nikal lo
        total_xor = 0
        for num in nums:
            total_xor = total_xor ^ num
            
        # Step 2: Total XOR aur k ke beech ka fark (difference) nikalo
        # XOR khud hi sirf unhi bits par 1 dega jo match NAHI karti hain
        diff = total_xor ^ k
        
        # Step 3: 'diff' ke andar total kitne set bits (1s) hain, wo gin lo.
        # Python mein iske liye .bit_count() inbuilt method hota hai (O(1) jaisa fast)
        # Agar purana Python version ho toh bin(diff).count('1') bhi use kar sakte hain
        return diff.bit_count()