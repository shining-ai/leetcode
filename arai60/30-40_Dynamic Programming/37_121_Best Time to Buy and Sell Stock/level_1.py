# Brute Force(TimeOut)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, buy_price in enumerate(prices):
            for sell_price in prices[i + 1 :]:
                profit = sell_price - buy_price
                max_profit = max(max_profit, profit)
        return max_profit


# 今までの価格の内最安値で買ったと仮定して、現在価格で売った場合の利益を計算する。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)
        return max_profit
