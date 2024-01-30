import collections


# O(n) space
# O(s) time
def solve_1(coins, amount):
    if amount == 0:
        return 0

    coins.sort(reverse=True)
    visited = set()
    queue = collections.deque([(0, 0)])

    while queue:
        coin_num, current_amount = queue.popleft()
        for i_coin in coins:
            if current_amount + i_coin == amount:
                return coin_num + 1
            elif current_amount + i_coin < amount:
                if current_amount + i_coin not in visited:
                    visited.add(current_amount + i_coin)
                    queue.append((coin_num + 1, current_amount + i_coin))

    return -1


if __name__ == "__main__":
    coins = [1]
    amount = 0
    print(solve_1(coins, amount))
