# BFSのように解く
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        remains_queue = deque([(amount, 0)])
        seen = set()
        while remains_queue:
            remain, coin_num = remains_queue.popleft()
            if remain == 0:
                return coin_num
            for coin in coins:
                next_remain = remain - coin
                if next_remain < 0:
                    continue
                if next_remain in seen:
                    continue
                remains_queue.append((next_remain, coin_num + 1))
                seen.add(next_remain)
        return -1
