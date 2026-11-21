from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_id = {}
        start_r = start_c = 0
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = len(litter_id)
                    
        num_litter = len(litter_id)
        if num_litter == 0:
            return 0
            
        target_mask = (1 << num_litter) - 1
        
        # max_energy[r][c][mask] tracks the highest energy seen at (r, c) with collected `mask`
        max_energy = [[[-1] * (1 << num_litter) for _ in range(n)] for _ in range(m)]
        max_energy[start_r][start_c][0] = energy
        
        q = deque([(start_r, start_c, 0, energy, 0)])  # (r, c, mask, rem_energy, moves)
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        while q:
            r, c, mask, rem_energy, moves = q.popleft()
            
            if rem_energy == 0:
                continue
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    nenergy = energy if classroom[nr][nc] == 'R' else rem_energy - 1
                    nmask = mask | (1 << litter_id[(nr, nc)]) if (nr, nc) in litter_id else mask
                    
                    if nmask == target_mask:
                        return moves + 1
                        
                    if nenergy > max_energy[nr][nc][nmask]:
                        max_energy[nr][nc][nmask] = nenergy
                        q.append((nr, nc, nmask, nenergy, moves + 1))
                        
        return -1