from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val = min(nums)
        max_val = max(nums)
        nums_set = set(nums)
        
        # Collect all integers in the range [min_val, max_val] not present in nums_set
        return [x for x in range(min_val, max_val + 1) if x not in nums_set]