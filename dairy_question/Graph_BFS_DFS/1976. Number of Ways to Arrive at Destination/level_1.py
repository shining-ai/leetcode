# ダイクストラで解いた
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007

        graph = defaultdict(list)
        for node1, node2, cost in roads:
            graph[node1].append((node2, cost))
            graph[node2].append((node1, cost))

        min_heap = [(0, 0)]
        shortest_time = [inf] * n
        path_count = [0] * n
        shortest_time[0] = 0
        path_count[0] = 1

        while min_heap:
            curr_time, curr_node = heappop(min_heap)
            if curr_time > shortest_time[curr_node]:
                continue
            for neighbor_node, road_time in graph[curr_node]:
                neighbor_time = curr_time + road_time
                if neighbor_time > shortest_time[neighbor_node]:
                    continue
                if neighbor_time == shortest_time[neighbor_node]:
                    path_count[neighbor_node] += path_count[curr_node]
                    path_count[neighbor_node] %= MOD
                    continue
                shortest_time[neighbor_node] = neighbor_time
                path_count[neighbor_node] = path_count[curr_node]
                heappush(
                    min_heap, (shortest_time[neighbor_node], neighbor_node))

        return path_count[n-1]
