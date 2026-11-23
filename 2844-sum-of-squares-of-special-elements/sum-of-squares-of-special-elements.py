class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        return sum(val * val for i, val in enumerate(nums, start=1) if n % i == 0)