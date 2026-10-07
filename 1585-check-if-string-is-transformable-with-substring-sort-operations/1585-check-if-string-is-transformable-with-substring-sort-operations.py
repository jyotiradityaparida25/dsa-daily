import collections

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = collections.defaultdict(collections.deque)
        for i, ch in enumerate(s):
            pos[int(ch)].append(i)
            
        for ch in t:
            digit = int(ch)
            if not pos[digit]:
                return False
                
            curr_idx = pos[digit][0]
            for d in range(digit):
                if pos[d] and pos[d][0] < curr_idx:
                    return False
                    
            pos[digit].popleft()
            
        return True