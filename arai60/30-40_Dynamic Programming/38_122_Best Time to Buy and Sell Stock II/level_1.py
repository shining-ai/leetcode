# 上昇傾向のときは前日買った分を売って利益を確定を繰り返す
# [1,2,3] は 1で買って3で売るのと、1で買って2で売って2で買って3で売るのと同じ
# 下降傾向のときは底値を探す
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy_price = prices[0]
        total_profit = 0
        for price in prices[1:]:
            if buy_price < price:
                total_profit += price - buy_price
                buy_price = price
                continue
            if buy_price > price:
                buy_price = price
        return total_profit
