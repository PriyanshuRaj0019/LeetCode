from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            count[char] += 1
            
            # If any character appears more than 2 times, shrink the window from the left
            while count[char] > 2:
                count[s[left]] -= 1
                left += 1
                
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len