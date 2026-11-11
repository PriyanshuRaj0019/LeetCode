from collections import Counter

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        
        # Collect positions of all 1s in both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        if not ones1 or not ones2:
            return 0
        
        # Count frequency of each shift vector (r2 - r1, c2 - c1)
        shifts = Counter((r2 - r1, c2 - c1) for r1, c1 in ones1 for r2, c2 in ones2)
        
        return max(shifts.values())