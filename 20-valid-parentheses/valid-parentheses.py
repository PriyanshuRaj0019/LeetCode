class Solution:
    def isValid(self, s: str) -> bool:
        # Quick parity check: odd length strings can never be balanced
        if len(s) % 2 != 0:
            return False

        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in bracket_map:
                # Top element if available, else a dummy placeholder
                top_element = stack.pop() if stack else '#'
                if bracket_map[ch] != top_element:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0