class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            # 1. Current number 'n' ke digits ka product nikalo
            prod = 1
            temp = n
            
            while temp > 0:
                prod = prod * (temp % 10)
                temp = temp // 10
                
            # 2. Check karo ki kya product 't' se completely divide hota hai?
            # (Agar product 0 hai, toh 0 % t == 0 hamesha True hoga!)
            if prod % t == 0:
                return n 
                
            # 3. Agar nahi hua, toh agle number ko check karo
            n += 1