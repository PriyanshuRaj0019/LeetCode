import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # free_servers: (weight, index)
        free_servers = [(weight, idx) for idx, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # busy_servers: (available_time, weight, index)
        busy_servers = []
        
        m = len(tasks)
        ans = [0] * m
        cur_time = 0
        
        for j, task_duration in enumerate(tasks):
            cur_time = max(cur_time, j)
            
            # Fast-forward time if no server is currently available
            if not free_servers:
                cur_time = max(cur_time, busy_servers[0][0])
            
            # Free up all servers that have finished by cur_time
            while busy_servers and busy_servers[0][0] <= cur_time:
                _, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))
            
            # Assign task j to the highest-priority free server
            weight, idx = heapq.heappop(free_servers)
            ans[j] = idx
            heapq.heappush(busy_servers, (cur_time + task_duration, weight, idx))
            
        return ans