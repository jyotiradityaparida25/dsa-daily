class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))
            events.append((R, 0, 0))
            
        events.sort()
        
        res = []
        hp = [(0, float('inf'))]
        
        for x, neg_h, R in events:
            while hp[0][1] <= x:
                heapq.heappop(hp)
                
            if neg_h != 0:
                heapq.heappush(hp, (neg_h, R))
                
            curr_max_h = -hp[0][0]
            if not res or res[-1][1] != curr_max_h:
                res.append([x, curr_max_h])
                
        return res