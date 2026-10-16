from collections import deque

class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        total_walls = 0
        
        def get_regions():
            visited = set()
            regions = []
            
            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and (r, c) not in visited:
                        region_cells = []
                        uninfected_neighbors = set()
                        walls_needed = 0
                        
                        queue = deque([(r, c)])
                        visited.add((r, c))
                        
                        while queue:
                            curr_r, curr_c = queue.popleft()
                            region_cells.append((curr_r, curr_c))
                            
                            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nr, nc = curr_r + dr, curr_c + dc
                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 1 and (nr, nc) not in visited:
                                        visited.add((nr, nc))
                                        queue.append((nr, nc))
                                    elif isInfected[nr][nc] == 0:
                                        walls_needed += 1
                                        uninfected_neighbors.add((nr, nc))
                                        
                        regions.append((uninfected_neighbors, walls_needed, region_cells))
            return regions

        while True:
            regions = get_regions()
            if not regions:
                break
                
            regions.sort(key=lambda x: len(x[0]), reverse=True)
            
            if len(regions[0][0]) == 0:
                break
                
            target_uninfected, walls_needed, target_cells = regions[0]
            total_walls += walls_needed
            for r, c in target_cells:
                isInfected[r][c] = 2
                
            for uninfected_neighbors, _, _ in regions[1:]:
                for r, c in uninfected_neighbors:
                    isInfected[r][c] = 1
                    
        return total_walls