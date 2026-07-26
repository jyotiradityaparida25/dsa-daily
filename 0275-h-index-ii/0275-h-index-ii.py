class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1
        
        while left <= right:
            mid = (left + right) // 2

            papers_remaining = n - mid
            
            if citations[mid] == papers_remaining:

                return papers_remaining
                
            elif citations[mid] < papers_remaining:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return n - left