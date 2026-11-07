class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0  # Min possible open brackets
        cmax = 0  # Max possible open brackets
        
        for ch in s:
            if ch == '(':
                cmin += 1
                cmax += 1
            elif ch == ')':
                cmin -= 1
                cmax -= 1
            else:  # ch == '*'
                cmin -= 1
                cmax += 1
            
            # More ')' than can ever be matched
            if cmax < 0:
                return False
            
            # Lower bound cannot be negative
            cmin = max(cmin, 0)
            
        return cmin == 0