class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
            
        buckets = {}
        bucket_size = valueDiff + 1
        
        for i, num in enumerate(nums):
            bucket = num // bucket_size
            
            if bucket in buckets:
                return True
                
            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True
                
            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True
                
            buckets[bucket] = num
            
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // bucket_size]
                
        return False
        