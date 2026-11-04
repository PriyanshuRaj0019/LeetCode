
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:

        MOD = 10**9 + 7

        positions = []
        prefix_sum = [0]
        prefix_num = [0]

        for i, ch in enumerate(s):
            digit = int(ch)

            if digit != 0:
                positions.append(i)

                prefix_sum.append(prefix_sum[-1] + digit)

                prefix_num.append(
                    (prefix_num[-1] * 10 + digit) % MOD
                )

        ans = []

        for l, r in queries:

            left = bisect_left(positions, l)
            right = bisect_right(positions, r)

            digit_sum = prefix_sum[right] - prefix_sum[left]

            number = (
                prefix_num[right]
                - prefix_num[left] * pow(10, right - left, MOD)
            ) % MOD

            ans.append((number * digit_sum) % MOD)

        return ans
