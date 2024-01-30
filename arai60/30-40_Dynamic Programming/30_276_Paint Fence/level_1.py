# O(n) time complexity
# O(n) space complexity
def solve_1(n, k):
    if n == 1:
        return k
    if n == 2:
        return k * k

    total_ways = [0] * (n + 1)
    total_ways[1] = k
    total_ways[2] = k * k

    for i in range(3, n + 1):
        total_ways[i] = (k - 1) * (total_ways[i - 1] + total_ways[i - 2])

    return total_ways[n]


def solve_2(n, k):
    def count_way(n):
        if n == 1:
            return k
        if n == 2:
            return k * k

        if n in total_ways:
            return total_ways[n]

        total_ways[n] = (k - 1) * (count_way(n - 1) + count_way(n - 2))
        return total_ways[n]

    total_ways = {}
    return count_way(n)


if __name__ == "__main__":
    n = 3
    k = 2
    print(solve_1(n, k))
    print(solve_2(n, k))
