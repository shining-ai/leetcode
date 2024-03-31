class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        yesterday_price = prices[0]
        total_profit = 0
        for today_price in prices[1:]:
            if yesterday_price < today_price:
                total_profit += today_price - yesterday_price
            yesterday_price = today_price
        return total_profit
