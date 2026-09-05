class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num
        
        answer = []
        for q in queries:
            idx = bisect_right(prefix, q) - 1
            answer.append(idx)
        
        return answer