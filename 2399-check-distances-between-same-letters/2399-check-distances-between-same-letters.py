class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first_occurrence = {}
        
        for i, char in enumerate(s):
            if char in first_occurrence:
                actual_distance = i - first_occurrence[char] - 1
                
                expected_distance = distance[ord(char) - ord('a')]
                
                if actual_distance != expected_distance:
                    return False
            else:
                first_occurrence[char] = i
                
        return True