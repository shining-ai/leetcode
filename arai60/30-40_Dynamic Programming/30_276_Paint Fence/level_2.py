# 同じ色で塗るパターンと違う色で塗るパターンを分けて考える
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k**2
        num_way = [0] * (n + 1)
        num_way[1] = k
        num_way[2] = k**2
        for i in range(3, n + 1):
            same_as_previous = (k - 1) * num_way[i - 2]
            different_from_previous = (k - 1) * num_way[i - 1]
            num_way[i] = same_as_previous + different_from_previous
        return num_way[-1]


# 1つ前と2つ前のパターンだけ記憶しておく
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k**2
        num_way_2_previous = k
        num_way_1_previous = k**2
        for i in range(3, n + 1):
            same_as_previous = (k - 1) * num_way_2_previous
            different_from_previous = (k - 1) * num_way_1_previous
            num_way = same_as_previous + different_from_previous
        return num_way


# メモ化(再帰)
class Solution:
    def numWays(self, n: int, k: int) -> int:
        num_way_memo = {}
        num_way_memo[1] = k
        num_way_memo[2] = k**2

        def count_num_way(n):
            if n in num_way_memo:
                return num_way_memo[n]
            same_as_previous = (k - 1) * count_num_way(n - 2)
            different_from_previous = (k - 1) * count_num_way(n - 1)
            num_way_memo[n] = same_as_previous + different_from_previous
            return num_way_memo[n]

        return count_num_way(n)


# メモ化(lru_cache)
def my_lru_cache(max_size=128):
    def decorator(func):
        cache = OrderedDict()

        def wrapper(*args):
            if args in cache:
                cache.move_to_end(args)
                return cache[args]
            result = func(*args)
            cache[args] = result
            if len(cache) > max_size:
                cache.popitem(last=False)
            return result

        return wrapper

    return decorator


class Solution:
    def numWays(self, n: int, k: int) -> int:
        @my_lru_cache(128)
        def count_num_way(n):
            if n == 1:
                return k
            if n == 2:
                return k**2
            same_as_previous = (k - 1) * count_num_way(n - 2)
            different_from_previous = (k - 1) * count_num_way(n - 1)
            return same_as_previous + different_from_previous

        return count_num_way(n)
