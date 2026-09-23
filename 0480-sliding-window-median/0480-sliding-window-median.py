class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        small = []
        large = []
        delayed = {}
        
        small_size = 0
        large_size = 0
        
        def prune(heap):
            while heap:
                val = -heap[0] if heap is small else heap[0]
                if delayed.get(val, 0) > 0:
                    delayed[val] -= 1
                    if delayed[val] == 0:
                        del delayed[val]
                    heapq.heappop(heap)
                else:
                    break

        def make_balance():
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                val = -heapq.heappop(small)
                heapq.heappush(large, val)
                small_size -= 1
                large_size += 1
                prune(small)
            elif small_size < large_size:
                val = heapq.heappop(large)
                heapq.heappush(small, -val)
                large_size -= 1
                small_size += 1
                prune(large)

        def add_num(num):
            nonlocal small_size, large_size
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1
            make_balance()

        def remove_num(num):
            nonlocal small_size, large_size
            delayed[num] = delayed.get(num, 0) + 1
            if num <= -small[0]:
                small_size -= 1
                if num == -small[0]:
                    prune(small)
            else:
                large_size -= 1
                if large and num == large[0]:
                    prune(large)
            make_balance()

        def get_median():
            if k % 2 == 1:
                return float(-small[0])
            else:
                return (-small[0] + large[0]) / 2.0

        for i in range(k):
            add_num(nums[i])

        res = [get_median()]

        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            res.append(get_median())

        return res