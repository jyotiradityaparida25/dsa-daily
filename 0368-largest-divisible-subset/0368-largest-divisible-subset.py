class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        nums.sort()
        n = len(nums)
        
        dp = [1] * n
        
        parent = [-1] * n
        
        max_size = 1
        max_index = 0
        
        for i in range(1, n):
            for j in range(i):
                
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
                        
                        if dp[i] > max_size:
                            max_size = dp[i]
                            max_index = i
                            
        res = []
        curr = max_index
        while curr != -1:
            res.append(nums[curr])
            curr = parent[curr]
            
        return res[::-1]