from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def ways(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            # Interleave elements of left and right subtrees
            interleaving_ways = comb(len(left) + len(right), len(left)) % MOD

            return (interleaving_ways * ways(left) * ways(right)) % MOD

        # Subtract 1 to exclude the original array permutation
        return (ways(nums) - 1) % MOD