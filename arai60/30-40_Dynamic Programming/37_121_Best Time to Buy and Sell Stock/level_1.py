# O(n) time complexity
# O(1) space complexity
def solve_1(princes):
    min_price = float("inf")
    max_profit = 0
    for i_price in prices:
        if i_price < min_price:
            min_price = i_price
        elif i_price - min_price > max_profit:
            max_profit = i_price - min_price
    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(solve_1(prices))
