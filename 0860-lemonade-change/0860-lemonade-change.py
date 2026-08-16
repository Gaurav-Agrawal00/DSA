class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hash_map = {}
        for b in bills:
            hash_map[b] = hash_map.get(b , 0) + 1 
            if b == 5:
                continue
            elif b == 10 :
                if hash_map.get(5,0) > 0 :
                    hash_map[5] -= 1
                else:
                    return False
            else:
                if  hash_map.get(10,0) > 0:
                    hash_map[10] -= 1

                    if hash_map.get(5,0) > 0 :
                        hash_map[5] -= 1
                    else:
                        return False

                elif  hash_map.get(5,0) >= 3:
                    hash_map[5] -= 3
                else:
                    return False
        return True