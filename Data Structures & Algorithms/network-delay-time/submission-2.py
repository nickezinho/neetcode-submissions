class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v,w))

        min_heap = [(0,k)]
        visited = set()
        max_time = 0

        while min_heap:
            cur_time, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            visited.add(node)

            max_time = max(max_time, cur_time)

            for ne, w in adj[node]:
                if ne not in visited:
                    heapq.heappush(min_heap, (cur_time + w, ne))
        return max_time if len(visited) == n else -1