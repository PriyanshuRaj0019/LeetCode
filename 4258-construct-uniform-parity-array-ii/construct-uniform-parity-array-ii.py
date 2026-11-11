class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        has_odd = any(x % 2 != 0 for x in nums1)
        
        # If the minimum value is odd, all numbers can be made odd.
        # If there are no odd numbers, all numbers are already even.
        return min_val % 2 != 0 or not has_odd