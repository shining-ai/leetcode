def solve_1(m, n):
    def combination(n, r):
        def kaijo(n):
            res = 1
            for i_n in range(n, 1, -1):
                res *= i_n

            return res

        res = kaijo(n) // (kaijo(r) * kaijo(n - r))
        return res

    go_num = (m - 1) + (n - 1)
    ans = combination(go_num, max(m - 1, n - 1))

    return ans


def solve_2(m, n):
    route_num = [[1] * n] * m

    for i_col in range(1, m):
        for i_row in range(1, n):
            route_num[i_col][i_row] = (
                route_num[i_col - 1][i_row] + route_num[i_col][i_row - 1]
            )

    return route_num[-1][-1]

if __name__ == "__main__":
    m = 3
    n = 7
    print(solve_1(m, n))
    print(solve_2(m, n))
