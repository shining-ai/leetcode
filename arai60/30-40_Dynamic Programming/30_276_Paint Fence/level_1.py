# 1つ前と別のいろで塗れるのは、k-1色
# 1つ前と同じ色で塗れるのは、2つ前と違う色のk-1色
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
            num_way[i] = (k - 1) * (num_way[i - 1] + num_way[i - 2])
        return num_way[-1]
