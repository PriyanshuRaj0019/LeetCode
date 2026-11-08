class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        # Feasibility check: maximum possible digit sum with `num` digits is 9 * num
        if sum_val > 9 * num:
            return ""
        
        # Determine how many 9s we can form and the leftover remainder
        nines, rem = divmod(sum_val, 9)
        
        # If the sum is an exact multiple of 9, pad the rest with 0s
        if rem == 0:
            return "9" * nines + "0" * (num - nines)
        
        # Otherwise, place all 9s, then the single remainder digit, then trailing 0s
        zeros = num - nines - 1
        return "9" * nines + str(rem) + "0" * zeros