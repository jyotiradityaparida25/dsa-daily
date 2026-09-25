import heapq

class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        
        heap = []
        total_time = 0
        
        for duration, last_day in courses:
            if total_time + duration <= last_day:
                heapq.heappush(heap, -duration)
                total_time += duration
            elif heap and -heap[0] > duration:
                total_time += duration + heapq.heappop(heap)
                heapq.heappush(heap, -duration)
                
        return len(heap)