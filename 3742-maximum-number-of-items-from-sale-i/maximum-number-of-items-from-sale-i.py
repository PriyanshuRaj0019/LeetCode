from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        
        # 1. Frequency of each factor and count of multiples
        freq = [0] * (max_factor + 1)
        for f, _ in items:
            freq[f] += 1
            
        multiples_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for m in range(f, max_factor + 1, f):
                    multiples_count[f] += freq[m]
                    
        # 2. 0/1 Knapsack for buying at most 1 copy of each item type
        dp = [-1] * (budget + 1)
        dp[0] = 0
        min_price = float('inf')
        
        for f, price in items:
            if price < min_price:
                min_price = price
            gain = multiples_count[f]  # 1 (itself) + (multiples_count[f] - 1) free copies
            
            for c in range(budget, price - 1, -1):
                if dp[c - price] != -1:
                    val = dp[c - price] + gain
                    if val > dp[c]:
                        dp[c] = val
                        
        # 3. Spend any leftover budget on the single cheapest item
        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                total = dp[c] + (budget - c) // min_price
                if total > ans:
                    ans = total
                    
        return ans