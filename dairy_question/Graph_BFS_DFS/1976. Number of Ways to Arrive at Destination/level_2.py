# ダイクストラ
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node1, node2, cost in roads:
            graph[node1].append((node2, cost))
            graph[node2].append((node1, cost))

        shortest_time = [inf] * n
        num_shortest_path = [0] * n
        shortest_time[0] = 0
        num_shortest_path[0] = 1
        min_heap = [(0, 0)]
        while min_heap:
            current_time, position = heappop(min_heap)
            for next_position, road_time in graph[position]:
                time_for_next = current_time + road_time
                if shortest_time[next_position] < time_for_next:
                    continue
                if shortest_time[next_position] == time_for_next:
                    num_shortest_path[next_position] += num_shortest_path[position]
                    num_shortest_path[next_position] %= 10**9 + 7
                    continue
                shortest_time[next_position] = time_for_next
                num_shortest_path[next_position] = num_shortest_path[position]
                heappush(min_heap, (time_for_next, next_position))
        return num_shortest_path[-1]
