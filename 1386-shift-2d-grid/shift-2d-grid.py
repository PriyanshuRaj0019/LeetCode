class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_idx = (i * n + j + k) % total
                res[new_idx // n][new_idx % n] = grid[i][j]
                
        return res