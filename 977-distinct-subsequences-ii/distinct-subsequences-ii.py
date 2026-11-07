class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # ends_with[c] stores distinct subsequences ending with character c
        ends_with = [0] * 26
        total = 0
        
        for ch in s:
            idx = ord(ch) - ord('a')
            # New distinct subsequences ending in ch
            new_ends_with = (total + 1) % MOD
            # Difference between new count and old count for this character
            added = (new_ends_with - ends_with[idx]) % MOD
            
            total = (total + added) % MOD
            ends_with[idx] = new_ends_with
            
        return total