from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_val = max(nums)
        return len(nums) * max_val - sum(nums)