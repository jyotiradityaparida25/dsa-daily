class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                
                count1 -= 1
                count2 -= 1
                
        result = []
        threshold = len(nums) // 3
        
        for c in (candidate1, candidate2):
            if c is not None and nums.count(c) > threshold:
                result.append(c)
                
        return result