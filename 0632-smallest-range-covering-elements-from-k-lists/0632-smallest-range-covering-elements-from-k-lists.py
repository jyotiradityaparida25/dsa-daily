class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        pq = []
        max_val = float('-inf')
        
        for i in range(len(nums)):
            heapq.heappush(pq, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
            
        range_start, range_end = float('-inf'), float('inf')
        
        while len(pq) == len(nums):
            min_val, list_idx, element_idx = heapq.heappop(pq)
            
            if max_val - min_val < range_end - range_start:
                range_start, range_end = min_val, max_val
                
            if element_idx + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][element_idx + 1]
                heapq.heappush(pq, (next_val, list_idx, element_idx + 1))
                max_val = max(max_val, next_val)
                
        return [range_start, range_end]