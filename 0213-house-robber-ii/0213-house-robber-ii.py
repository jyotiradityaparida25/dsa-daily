class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        def rob_straight_street(houses):
            prev_max = 0
            curr_max = 0
            for money in houses:
                new_max = max(money + prev_max, curr_max)
                prev_max = curr_max
                curr_max = new_max
            return curr_max
            
        max_without_last = rob_straight_street(nums[:-1])
        
        max_without_first = rob_straight_street(nums[1:])
        
        return max(max_without_last, max_without_first)