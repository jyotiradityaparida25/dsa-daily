import collections

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        pos = collections.defaultdict(collections.deque)
        for i, ch in enumerate(num):
            pos[int(ch)].append(i + 1)
            
        tree = [0] * (n + 1)
        
        def update(idx: int, val: int):
            while idx <= n:
                tree[idx] += val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            s = 0
            while idx > 0:
                s += tree[idx]
                idx -= idx & (-idx)
            return s
            
        for i in range(1, n + 1):
            update(i, 1)
            
        ans = []
        
        for _ in range(n):
            for d in range(10):
                if pos[d]:
                    orig_idx = pos[d][0]
                    curr_pos = query(orig_idx)
                    cost = curr_pos - 1
                    
                    if cost <= k:
                        k -= cost
                        ans.append(str(d))
                        update(orig_idx, -1)
                        pos[d].popleft()
                        break
                        
        return "".join(ans)