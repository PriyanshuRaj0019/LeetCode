class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        digit_sum = 0
        digit_prod = 1

        while temp > 0:
            d = temp % 10
            digit_sum += d
            digit_prod *= d
            temp //= 10

        total = digit_sum + digit_prod
        return n % total == 0