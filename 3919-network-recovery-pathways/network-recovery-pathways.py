from collections import deque

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        unique_costs = set()

        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                in_degree[v] += 1
                unique_costs.add(cost)

        # Topological sort (Kahn's algorithm) computed once
        topo = []
        q = deque(i for i in range(n) if in_degree[i] == 0 and online[i])
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)

        if not unique_costs:
            return -1

        sorted_costs = sorted(unique_costs)
        INF = k + 1

        def can_reach(min_cost: int) -> bool:
            dist = [INF] * n
            dist[0] = 0
            for u in topo:
                d = dist[u]
                if d > k:
                    continue
                if u == n - 1:
                    return True
                for v, cost in adj[u]:
                    if cost >= min_cost and d + cost < dist[v]:
                        dist[v] = d + cost
            return dist[n - 1] <= k

        left, right = 0, len(sorted_costs) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if can_reach(sorted_costs[mid]):
                ans = sorted_costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return ans