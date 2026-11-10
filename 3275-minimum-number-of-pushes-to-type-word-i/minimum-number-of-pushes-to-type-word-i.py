class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        q, r = divmod(n, 8)
        # Sum for q full blocks: 8 * (1 + 2 + ... + q) = 8 * q * (q + 1) // 2 = 4 * q * (q + 1)
        # Plus the remainder r letters each costing (q + 1) pushes
        return 4 * q * (q + 1) + r * (q + 1)