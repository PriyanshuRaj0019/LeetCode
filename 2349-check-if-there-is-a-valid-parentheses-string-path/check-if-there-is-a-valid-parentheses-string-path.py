from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [0] * n
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    prev = 1  # Balance 0 before processing (0, 0)
                else:
                    prev = dp[c] | (dp[c - 1] if c > 0 else 0)

                dp[c] = (prev << 1) if grid[r][c] == '(' else (prev >> 1)

        return bool(dp[-1] & 1)