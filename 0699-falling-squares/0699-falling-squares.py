class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        heights = []
        ans = []
        max_h = 0
        
        for i, (l1, side1) in enumerate(positions):
            r1 = l1 + side1
            base_height = 0
            
            for j in range(i):
                l2, side2 = positions[j]
                r2 = l2 + side2
                
                if l1 < r2 and l2 < r1:
                    base_height = max(base_height, heights[j])
                    
            current_h = base_height + side1
            heights.append(current_h)
            max_h = max(max_h, current_h)
            ans.append(max_h)
            
        return ans