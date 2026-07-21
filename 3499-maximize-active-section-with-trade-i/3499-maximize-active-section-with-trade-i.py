class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = 0
        
        # In variables mein hum 0-blocks ki length store karenge
        prev_zeros = 0
        curr_zeros = 0
        max_gain = 0
        
        for char in s:
            if char == '1':
                initial_ones += 1
                
                # Agar hum just ek 0-block cross karke aaye hain
                if curr_zeros > 0:
                    # Agar isse pehle bhi ek 0-block tha, toh dono ko jod kar dekho
                    if prev_zeros > 0:
                        max_gain = max(max_gain, prev_zeros + curr_zeros)
                    
                    # Ab aage badhne ke liye current block, previous ban jayega
                    prev_zeros = curr_zeros
                    curr_zeros = 0
            else:
                # Agar '0' mila, toh current zero block ki length badhao
                curr_zeros += 1
                
        # Loop khatam hone ke baad, agar aakhiri mein koi 0-block bacha tha toh use bhi check karo
        if curr_zeros > 0:
            if prev_zeros > 0:
                max_gain = max(max_gain, prev_zeros + curr_zeros)
            
        # Final answer = Pehle se jitne 1 the + Trade karke jo naye 1 mile
        return initial_ones + max_gain