class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        bus_in_route = defaultdict(set)
        for route, stops in enumerate(routes):
            for bus_stop in stops:
                bus_in_route[bus_stop].add(route)

        queue = deque()
        next_queue = deque(list(bus_in_route[source]))
        seen = set(bus_in_route[source])
        bus_count = 1

        while next_queue:
            queue = next_queue
            next_queue = deque()
            while queue:
                route = queue.popleft()
                for stop in routes[route]:
                    if stop == target:
                        return bus_count
                    for next_route in bus_in_route[stop]:
                        if next_route in seen:
                            continue
                        seen.add(next_route)
                        next_queue.append(next_route)
            bus_count += 1
        return -1
