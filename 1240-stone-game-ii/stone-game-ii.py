class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum[i]
                else:
                    min_opponent = float('inf')
                    for x in range(1, 2 * m + 1):
                        next_m = max(m, x)
                        min_opponent = min(min_opponent, dp[i + x][next_m])
                    dp[i][m] = suffix_sum[i] - min_opponent
                    
        return dp[0][1]