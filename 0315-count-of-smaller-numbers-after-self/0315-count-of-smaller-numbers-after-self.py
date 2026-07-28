class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)

        indices = list(range(n))
        result = [0] * n
        
        def merge_sort(left: int, right: int):
            if left >= right:
                return
            
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            
            temp = []
            i = left
            j = mid + 1
            right_counter = 0  
            
            while i <= mid and j <= right:
               
                if nums[indices[j]] < nums[indices[i]]:
                    right_counter += 1
                    temp.append(indices[j])
                    j += 1
                else:
                    
                    result[indices[i]] += right_counter
                    temp.append(indices[i])
                    i += 1
                    
            while i <= mid:
                result[indices[i]] += right_counter
                temp.append(indices[i])
                i += 1
                
            while j <= right:
                temp.append(indices[j])
                j += 1
                
            for k in range(left, right + 1):
                indices[k] = temp[k - left]
                
        merge_sort(0, n - 1)
        
        return result