# OnePass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price_until = math.inf
        for price in prices:
            if price < min_price_until:
                min_price_until = price
            max_profit = max(max_profit, price - min_price_until)
        return max_profit
