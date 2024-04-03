# BFS的なアプローチ
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(amount, 0)])
        seen = set([amount])
        while queue:
            remaining_amount, num_coin = queue.popleft()
            if remaining_amount == 0:
                return num_coin
            for coin in coins:
                if remaining_amount - coin < 0:
                    continue
                if remaining_amount - coin in seen:
                    continue
                queue.append((remaining_amount - coin, num_coin + 1))
                seen.add(remaining_amount - coin)
        return -1
