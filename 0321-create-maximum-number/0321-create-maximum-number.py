class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def get_max_subsequence(nums, length):
            stack = []
            drop = len(nums) - length 
            
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
                
            return stack[:length]
        
        def merge(seq1, seq2):
            ans = []
            
            while seq1 or seq2:
                if seq1 > seq2:
                    ans.append(seq1.pop(0))
                else:
                    ans.append(seq2.pop(0))
            return ans

        m, n = len(nums1), len(nums2)
        best_result = []
        
        for i in range(max(0, k - n), min(k, m) + 1):
            sub1 = get_max_subsequence(nums1, i)
            sub2 = get_max_subsequence(nums2, k - i)
            
            merged = merge(sub1, sub2)
            best_result = max(best_result, merged)
            
        return best_result