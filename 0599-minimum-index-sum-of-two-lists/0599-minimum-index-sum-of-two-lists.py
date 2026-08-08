class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {s: i for i, s in enumerate(list1)}
        best_sum = float('inf')
        result = []
        
        for j, s in enumerate(list2):
            if s in index1:
                total = index1[s] + j
                if total < best_sum:
                    best_sum = total
                    result = [s]
                elif total == best_sum:
                    result.append(s)
        
        return result