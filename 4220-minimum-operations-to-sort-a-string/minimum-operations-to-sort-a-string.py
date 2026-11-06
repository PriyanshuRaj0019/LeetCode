from itertools import pairwise

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # Case 0: Already sorted
        if all(a <= b for a, b in pairwise(s)):
            return 0
        
        # Case -1: Length 2 cannot be modified with proper substrings
        if n == 2:
            return -1
        
        mn = min(s)
        mx = max(s)
        
        # Case 1: Extremal element already in place at either end
        if s[0] == mn or s[-1] == mx:
            return 1
        
        # Case 2: Extremal element exists in the interior
        if any(c == mn or c == mx for c in s[1:-1]):
            return 2
        
        # Case 3: mn is at index -1 and mx is at index 0
        return 3