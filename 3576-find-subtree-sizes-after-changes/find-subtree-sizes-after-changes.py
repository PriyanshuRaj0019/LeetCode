import sys
sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = parent[:]
        last_seen = [-1] * 26
        
        def dfs_reparent(u: int) -> None:
            c = ord(s[u]) - ord('a')
            prev = last_seen[c]
            if prev != -1:
                new_parent[u] = prev
            last_seen[c] = u
            
            for v in adj[u]:
                dfs_reparent(v)
                
            last_seen[c] = prev
            
        dfs_reparent(0)
        
        # Build the updated tree and compute subtree sizes
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        answer = [1] * n
        
        def dfs_size(u: int) -> int:
            total = 1
            for v in new_adj[u]:
                total += dfs_size(v)
            answer[u] = total
            return total
            
        dfs_size(0)
        return answer