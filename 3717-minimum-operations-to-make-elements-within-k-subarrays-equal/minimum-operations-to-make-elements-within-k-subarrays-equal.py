
from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        low = SortedList()
        high = SortedList()
        total_low = 0
        total_high = 0

        costs = [0] * (n - x + 1)

        def add(num):
            nonlocal total_low, total_high

            if not low or num <= low[-1]:
                low.add(num)
                total_low += num
            else:
                high.add(num)
                total_high += num

            balance()

        def remove(num):
            nonlocal total_low, total_high

            if num in low:
                low.remove(num)
                total_low -= num
            else:
                high.remove(num)
                total_high -= num

            balance()

        def balance():
            nonlocal total_low, total_high

            while len(low) > len(high) + 1:
                num = low.pop()
                total_low -= num
                high.add(num)
                total_high += num

            while len(low) < len(high):
                num = high.pop(0)
                total_high -= num
                low.add(num)
                total_low += num

        def get_cost():
            median = low[-1]

            left_cost = median * len(low) - total_low
            right_cost = total_high - median * len(high)

            return left_cost + right_cost

        for i in range(n):
            add(nums[i])

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                costs[i - x + 1] = get_cost()

        INF = float('inf')

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]

                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + costs[i - x]
                    )

        return dp[n][k]
