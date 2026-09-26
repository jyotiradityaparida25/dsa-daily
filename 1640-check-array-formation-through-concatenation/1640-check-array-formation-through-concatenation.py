class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        start_map = {p[0]: p for p in pieces}
        
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] not in start_map:
                return False
            piece = start_map[arr[i]]
            
            for num in piece:
                if i >= n or arr[i] != num:
                    return False
                i += 1
        return True