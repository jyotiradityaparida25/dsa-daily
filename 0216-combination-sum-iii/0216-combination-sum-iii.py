class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        
        def backtrack(start_num, current_combo, current_sum):
            if len(current_combo) == k:
                if current_sum == n:
                    results.append(list(current_combo))
                return 
            
            if current_sum > n:
                return 
            
            for i in range(start_num, 10):
                current_combo.append(i)
                
                backtrack(i + 1, current_combo, current_sum + i)
                
                current_combo.pop()

        backtrack(1, [], 0)
        
        return results