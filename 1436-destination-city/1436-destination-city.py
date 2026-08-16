class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departures = set()
        for path in paths:
            departures.add(path[0])
            
        for path in paths:
            destination = path[1]
            if destination not in departures:
                return destination