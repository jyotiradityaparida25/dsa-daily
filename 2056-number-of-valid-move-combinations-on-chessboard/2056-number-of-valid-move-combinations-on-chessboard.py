class Solution:
    def countCombinations(self, pieces: list[str], positions: list[list[int]]) -> int:
        n = len(pieces)
        
        directions = {
            'rook': [(1, 0), (-1, 0), (0, 1), (0, -1)],
            'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            'queen': [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        }
        
        all_piece_moves = []
        for i in range(n):
            r, c = positions[i]
            piece_moves = [((r, c), (0, 0), 0)]  # Stay in place
            
            for dr, dc in directions[pieces[i]]:
                nr, nc = r + dr, c + dc
                step = 1
                while 1 <= nr <= 8 and 1 <= nc <= 8:
                    piece_moves.append(((r, c), (dr, dc), step))
                    nr += dr
                    nc += dc
                    step += 1
                    
            all_piece_moves.append(piece_moves)
            
        def is_valid_pair(m1, m2):
            (r1, c1), (dr1, dc1), step1 = m1
            (r2, c2), (dr2, dc2), step2 = m2
            
            max_t = max(step1, step2)
            for t in range(1, max_t + 1):
                cur_r1 = r1 + dr1 * min(t, step1)
                cur_c1 = c1 + dc1 * min(t, step1)
                
                cur_r2 = r2 + dr2 * min(t, step2)
                cur_c2 = c2 + dc2 * min(t, step2)
                
                if cur_r1 == cur_r2 and cur_c1 == cur_c2:
                    return False
            return True

        valid_combinations = 0

        def backtrack(idx, current_moves):
            nonlocal valid_combinations
            if idx == n:
                valid_combinations += 1
                return
            
            for move in all_piece_moves[idx]:
                valid = True
                for prev_move in current_moves:
                    if not is_valid_pair(prev_move, move):
                        valid = False
                        break
                if valid:
                    current_moves.append(move)
                    backtrack(idx + 1, current_moves)
                    current_moves.pop()

        backtrack(0, [])
        return valid_combinations