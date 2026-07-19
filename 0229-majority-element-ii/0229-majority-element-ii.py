class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        el1  = nums[0]
        cnt1 = 0
        cnt2 = 0
        el2 = float('inf')

        for num in nums:
            if cnt1 == 0 and num != el2:
                el1 = num

            if cnt2 == 0 and num != el1:
                el2 = num
            
            if num == el1 :
                cnt1 += 1
            elif num == el2 :
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
            
        cnt1 = 0
        cnt2 = 0
        min_occ = len(nums)//3
        for num in nums:
            if num == el1 :
                cnt1 +=1
            elif num == el2 :
                cnt2 += 1
        
        if cnt2 > min_occ and cnt1 > min_occ:
            return [el1,el2]

        elif cnt1 > min_occ :
            return [el1]
        elif cnt2 > min_occ:
            return [el2]
        else:
            return []