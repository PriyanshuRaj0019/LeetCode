from collections import deque
from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        # 1. Mark all methods reachable from k as suspicious
        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])

        while queue:
            curr = queue.popleft()
            for nxt in adj[curr]:
                if not suspicious[nxt]:
                    suspicious[nxt] = True
                    queue.append(nxt)

        # 2. Check if any non-suspicious method invokes a suspicious one
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # 3. Safe to remove all suspicious methods
        return [i for i in range(n) if not suspicious[i]]