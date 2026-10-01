class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        for id in range(left, right + 1):
            if not any(start <= id <= end for start, end in ranges):
                return False
        return True