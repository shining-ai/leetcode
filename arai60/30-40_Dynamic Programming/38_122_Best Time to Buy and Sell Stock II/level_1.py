# O(n) time complexity
# O(1) space complexity
def solve_1(prices):
    buy_price = prices[0]
    profit = 0

    for i_price in prices:
        if i_price < buy_price:
            buy_price = i_price
        elif i_price > buy_price:
            profit += i_price - buy_price
            buy_price = i_price

    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(solve_1(prices))
