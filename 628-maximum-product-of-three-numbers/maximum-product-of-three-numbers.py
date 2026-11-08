from typing import List
import math

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Track the 3 largest values: max1 >= max2 >= max3
        max1 = max2 = max3 = -math.inf
        # Track the 2 smallest values: min1 <= min2
        min1 = min2 = math.inf

        for x in nums:
            # Update the top 3 maximums
            if x > max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                max3 = max2
                max2 = x
            elif x > max3:
                max3 = x

            # Update the bottom 2 minimums
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

        return max(max1 * max2 * max3, min1 * min2 * max1)