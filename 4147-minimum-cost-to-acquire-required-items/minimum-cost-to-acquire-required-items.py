class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        m = min(need1, need2)
        M = max(need1, need2)
        
        # Option 1: Individual purchases only
        opt1 = need1 * cost1 + need2 * cost2
        
        # Option 2: Bundles for the overlap, individual for the remainder
        opt2 = m * costBoth + (need1 - m) * cost1 + (need2 - m) * cost2
        
        # Option 3: Bundles covering up to the maximum requirement
        opt3 = M * costBoth
        
        return min(opt1, opt2, opt3)