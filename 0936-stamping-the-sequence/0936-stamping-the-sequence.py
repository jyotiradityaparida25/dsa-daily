class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        m, n = len(stamp), len(target)
        target_list = list(target)
        res = []
        visited = [False] * (n - m + 1)
        stars = 0

        def can_stamp(idx: int) -> bool:
            matched = False
            for i in range(m):
                if target_list[idx + i] == '?':
                    continue
                if target_list[idx + i] != stamp[i]:
                    return False
                matched = True
            return matched

        def do_stamp(idx: int) -> int:
            nonlocal stars
            count = 0
            for i in range(m):
                if target_list[idx + i] != '?':
                    target_list[idx + i] = '?'
                    count += 1
            stars += count
            return count

        while stars < n:
            stamped = False
            for i in range(n - m + 1):
                if not visited[i] and can_stamp(i):
                    do_stamp(i)
                    visited[i] = True
                    stamped = True
                    res.append(i)
                    if stars == n:
                        break
            if not stamped:
                return []

        return res[::-1]