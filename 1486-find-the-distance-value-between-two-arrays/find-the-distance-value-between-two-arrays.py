import bisect
from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        
        for x in arr1:
            # Find the first element in arr2 that is >= x - d
            idx = bisect.bisect_left(arr2, x - d)
            
            # If idx is within bounds and the element is <= x + d, a violation exists
            if idx < len(arr2) and arr2[idx] <= x + d:
                continue
            
            count += 1
            
        return count