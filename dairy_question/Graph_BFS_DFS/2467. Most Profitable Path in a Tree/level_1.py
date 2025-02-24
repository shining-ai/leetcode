class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        path = defaultdict(set)
        for edge1, edge2 in edges:
            path[edge1].add(edge2)
            path[edge2].add(edge1)

        bobs_route = deque()
        seen = set()

        def find_bobs_route(current):
            if current == 0:
                bobs_route.append(current)
                return True
            seen.add(current)
            for next_pos in path[current]:
                if next_pos in seen:
                    continue
                if find_bobs_route(next_pos):
                    bobs_route.append(current)
                    return True
            return False
        find_bobs_route(bob)

        next_queue = deque([(0, 0)])
        max_profit = -inf
        seen = set()
        bob_pos = bobs_route.pop()
        while next_queue:
            alice_queue = next_queue
            next_queue = deque()
            while alice_queue:
                alice_pos, profit = alice_queue.popleft()
                profit += amount[alice_pos]
                if alice_pos == bob_pos:
                    profit -= amount[alice_pos] // 2
                if not path[alice_pos]:
                    max_profit = max(max_profit, profit)
                    continue
                for alice_next in path[alice_pos]:
                    path[alice_next].discard(alice_pos)
                    next_queue.append((alice_next, profit))
            amount[bob_pos] = 0
            if bobs_route:
                bob_pos = bobs_route.pop()
        return max_profit
