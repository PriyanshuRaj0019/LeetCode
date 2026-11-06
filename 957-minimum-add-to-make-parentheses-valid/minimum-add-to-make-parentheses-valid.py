class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0      # Unmatched ')' needing '('
        unmatched_open = 0   # Unmatched '(' needing ')'
        
        for ch in s:
            if ch == '(':
                unmatched_open += 1
            else:  # ch == ')'
                if unmatched_open > 0:
                    unmatched_open -= 1
                else:
                    open_needed += 1
                    
        return open_needed + unmatched_open