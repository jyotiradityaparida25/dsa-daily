class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = Counter(arr1)
        result = []
        
        for num in arr2:
            if num in counts:
                result.extend([num] * counts[num])
                del counts[num]  
                
        leftovers = []
        for num, count in counts.items():
            leftovers.extend([num] * count)
            
        leftovers.sort()
        
        return result + leftovers