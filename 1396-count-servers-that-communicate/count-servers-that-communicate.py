from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n
        servers = []

        # Pass 1: Count servers per row/column and record server coordinates
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1
                    servers.append((r, c))

        # Pass 2: Check only the recorded servers instead of the entire m * n grid
        communicating_servers = 0
        for r, c in servers:
            if row_count[r] > 1 or col_count[c] > 1:
                communicating_servers += 1

        return communicating_servers