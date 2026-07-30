class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        def merge_sort(lo: int, hi: int) -> int:
            
            if hi - lo <= 1:
                return 0
                
            mid = (lo + hi) // 2
            
            count = merge_sort(lo, mid) + merge_sort(mid, hi)
            
            j1 = j2 = mid
            for i in range(lo, mid):
            
                while j1 < hi and prefix[j1] - prefix[i] < lower:
                    j1 += 1
                
                while j2 < hi and prefix[j2] - prefix[i] <= upper:
                    j2 += 1
                
                count += (j2 - j1)
                
            temp = []
            left, right = lo, mid
            
            while left < mid and right < hi:
                if prefix[left] <= prefix[right]:
                    temp.append(prefix[left])
                    left += 1
                else:
                    temp.append(prefix[right])
                    right += 1
                    
            while left < mid:
                temp.append(prefix[left])
                left += 1
            while right < hi:
                temp.append(prefix[right])
                right += 1
                
            prefix[lo:hi] = temp
            
            return count

        return merge_sort(0, len(prefix))