class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not set(s2).issubset(set(s1)):
            return 0
            
        len1, len2 = len(s1), len(s2)
        
        recall = {} 
        
        s1_count = 0
        s2_count = 0
        index = 0
        
        while s1_count < n1:
            
            for char in s1:
                if char == s2[index]:
                    index += 1
                    if index == len2:
                        s2_count += 1
                        index = 0
            
            s1_count += 1
            
            if index in recall:
                
                prev_s1_count, prev_s2_count = recall[index]
                
                cycle_len_s1 = s1_count - prev_s1_count

                cycle_len_s2 = s2_count - prev_s2_count
                
                remaining_s1 = n1 - s1_count
                num_cycles = remaining_s1 // cycle_len_s1
                
                s1_count += num_cycles * cycle_len_s1
                s2_count += num_cycles * cycle_len_s2
                
                recall.clear()
            else:
                recall[index] = (s1_count, s2_count)
                
        return s2_count // n2