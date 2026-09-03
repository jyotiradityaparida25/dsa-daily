class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def resolve(b: str) -> str:
            while True:
                for i in range(len(b)):
                    j = i
                    
                    while j < len(b) and b[j] == b[i]:
                        j += 1
                    
                    if j - i >= 3:
                        b = b[:i] + b[j:]
                        break
                else:
                    
                    break 
            return b

        hand = "".join(sorted(hand))
        queue = deque([(board, hand, 0)])
        visited = {(board, hand)}

        while queue:
            b, h, step = queue.popleft()

            if not b:
                return step
            
            if not h:
                continue

            for c in set(h):
              
                new_h = h.replace(c, '', 1)

                for i in range(len(b) + 1):
                    
                    if (i < len(b) and b[i] == c) or \
                       (i > 0 and i < len(b) and b[i-1] == b[i] and b[i] != c):
                        
                        new_b = resolve(b[:i] + c + b[i:])
                        
                        if (new_b, new_h) not in visited:
                            visited.add((new_b, new_h))
                            queue.append((new_b, new_h, step + 1))

        return -1