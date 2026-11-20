from collections import defaultdict

class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        
        for x in nums:
            # Update x + 1 first so a single element doesn't chain onto itself
            dp[x + 1] = max(dp[x + 1], dp[x] + 1)
            dp[x] = max(dp[x], dp[x - 1] + 1)
            
        return max(dp.values())