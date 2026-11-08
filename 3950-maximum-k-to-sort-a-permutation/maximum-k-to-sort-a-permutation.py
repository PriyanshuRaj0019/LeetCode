from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Start with all bits set (-1 in two's complement represents infinite 1s)
        ans = -1
        
        for i, val in enumerate(nums):
            if i != val:
                ans &= val
                
        # If ans is still -1, no elements were out of place (already sorted)
        return 0 if ans == -1 else ans