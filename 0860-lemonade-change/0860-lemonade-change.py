class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else: # b == 20
                # Hamesha greedy bano: pehle $10 ka note nikalne ki koshish karo
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
                    
        return True
