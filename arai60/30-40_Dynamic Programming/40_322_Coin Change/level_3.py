class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(amount, 0)])
        seen = set([amount])
        while queue:
            remain_amount, num_coin = queue.popleft()
            if remain_amount == 0:
                return num_coin
            for coin in coins:
                next_amount = remain_amount - coin
                if next_amount < 0:
                    continue
                if next_amount in seen:
                    continue
                queue.append((next_amount, num_coin + 1))
                seen.add(next_amount)
        return -1
