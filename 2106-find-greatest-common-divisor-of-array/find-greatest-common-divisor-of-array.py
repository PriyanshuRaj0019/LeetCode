
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)

        while largest:
            smallest, largest = largest, smallest % largest

        return smallest
