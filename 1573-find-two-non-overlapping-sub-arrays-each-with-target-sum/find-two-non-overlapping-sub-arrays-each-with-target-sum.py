from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        # best[i] stores the minimum length of a valid sub-array ending at or before index i
        best = [float('inf')] * n
        
        left = 0
        curr_sum = 0
        min_ans = float('inf')
        current_best_len = float('inf')
        
        for right in range(n):
            curr_sum += arr[right]
            
            # Shrink the window while the sum exceeds target
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            # If we found a valid sub-array summing to target
            if curr_sum == target:
                length = right - left + 1
                
                # Check if there is a non-overlapping valid sub-array to the left
                if left > 0 and best[left - 1] != float('inf'):
                    min_ans = min(min_ans, length + best[left - 1])
                
                # Track the minimum length of a valid sub-array ending at or before `right`
                current_best_len = min(current_best_len, length)
            
            best[right] = current_best_len
            
        return min_ans if min_ans != float('inf') else -1