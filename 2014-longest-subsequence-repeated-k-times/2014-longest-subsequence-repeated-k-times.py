from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        counts = Counter(s)
        candidates = sorted([ch for ch, freq in counts.items() if freq >= k], reverse=True)
        
        def is_subsequence(target: str) -> bool:
            full_target = target * k
            it = iter(s)
            return all(char in it for char in full_target)

        queue = deque([""])
        ans = ""

        while queue:
            curr = queue.popleft()
            
            for ch in candidates:
                nxt = curr + ch
                if is_subsequence(nxt):
                    if len(nxt) > len(ans) or (len(nxt) == len(ans) and nxt > ans):
                        ans = nxt
                    queue.append(nxt)

        return ans