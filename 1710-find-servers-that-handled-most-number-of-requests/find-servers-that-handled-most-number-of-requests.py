import heapq
from typing import List

class SegmentTree:
    """A point-update, range-query Segment Tree to find the first available server."""
    def __init__(self, size: int):
        self.n = size
        # 1 means available, 0 means busy
        self.tree = [0] * (4 * size)
        self._build(0, 0, size - 1)

    def _build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = 1
            return
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid)
        self._build(2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        """Finds the first available server index in range [l, r]. Returns -1 if none."""
        if r < start or end < l or self.tree[node] == 0:
            return -1
        if start == end:
            return start
        mid = (start + end) // 2
        res = self.query(2 * node + 1, start, mid, l, r)
        if res != -1:
            return res
        return self.query(2 * node + 2, mid + 1, end, l, r)


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy_heap = []  # Stores tuples of (free_time, server_id)
        seg_tree = SegmentTree(k)
        request_count = [0] * k

        for i, (arr_time, l_time) in enumerate(zip(arrival, load)):
            # 1. Free up servers whose tasks have completed by arr_time
            while busy_heap and busy_heap[0][0] <= arr_time:
                _, sid = heapq.heappop(busy_heap)
                seg_tree.update(0, 0, k - 1, sid, 1)

            # If no servers are available at all, drop the request
            if seg_tree.tree[0] == 0:
                continue

            preferred = i % k
            # 2. Try to find an available server from preferred to k - 1
            server_id = seg_tree.query(0, 0, k - 1, preferred, k - 1)
            # 3. If none found, wrap around and search from 0 to preferred - 1
            if server_id == -1:
                server_id = seg_tree.query(0, 0, k - 1, 0, preferred - 1)

            # Assign the request to the found server
            seg_tree.update(0, 0, k - 1, server_id, 0)
            heapq.heappush(busy_heap, (arr_time + l_time, server_id))
            request_count[server_id] += 1

        # Find all servers with the maximum request count
        max_requests = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_requests]