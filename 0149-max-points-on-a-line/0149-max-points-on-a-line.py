class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
            
        max_pts = 0
        
        for i in range(len(points)):
            slopes = defaultdict(int)
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                    
                slope = (dx, dy)
                slopes[slope] += 1
                
            if slopes:
                max_pts = max(max_pts, max(slopes.values()) + 1)
                
        return max_pts