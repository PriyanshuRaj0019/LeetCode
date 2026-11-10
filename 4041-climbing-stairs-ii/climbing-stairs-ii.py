class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        # dp0 represents dp[i - 3], dp1 represents dp[i - 2], dp2 represents dp[i - 1]
        dp0 = float('inf')
        dp1 = float('inf')
        dp2 = 0  # dp[0] = 0

        for i in range(1, n + 1):
            c = costs[i - 1]
            cur_dp = c + min(dp2 + 1, dp1 + 4, dp0 + 9)
            
            # Slide window forward
            dp0 = dp1
            dp1 = dp2
            dp2 = cur_dp

        return dp2