class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp1 = dp2 = dp3 = 0  # Represents dp[i+1], dp[i+2], dp[i+3]

        for i in range(n - 1, -1, -1):
            # Take 1 stone
            take_sum = stoneValue[i]
            best = take_sum - dp1

            # Take 2 stones
            if i + 1 < n:
                take_sum += stoneValue[i + 1]
                best = max(best, take_sum - dp2)

            # Take 3 stones
            if i + 2 < n:
                take_sum += stoneValue[i + 2]
                best = max(best, take_sum - dp3)

            dp3, dp2, dp1 = dp2, dp1, best

        if dp1 > 0:
            return "Alice"
        if dp1 < 0:
            return "Bob"
        return "Tie"