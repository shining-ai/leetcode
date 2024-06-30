# Top down DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def calculate_fewest_coin(remaining_amount):
            if remaining_amount == 0:
                return 0
            min_count = math.inf
            for coin in coins:
                if remaining_amount - coin < 0:
                    continue
                current_count = calculate_fewest_coin(remaining_amount - coin)
                if current_count != -1:
                    min_count = min(min_count, current_count + 1)
            if min_count == math.inf:
                return -1
            return min_count

        return calculate_fewest_coin(amount)


# Bottom up DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        fewest_coins = [math.inf] * (amount + 1)
        fewest_coins[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if fewest_coins[i - coin] == math.inf:
                    continue
                fewest_coins[i] = min(
                    fewest_coins[i], fewest_coins[i - coin] + 1
                )
        if fewest_coins[-1] == math.inf:
            return -1
        return fewest_coins[-1]
