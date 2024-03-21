class Solution:
    def numWays(self, n: int, k: int) -> int:
        num_way_map = {}
        num_way_map[1] = k
        num_way_map[2] = k**2
        for i in range(3, n + 1):
            same_as_previous = (k - 1) * num_way_map[i - 2]
            different_from_previous = (k - 1) * num_way_map[i - 1]
            num_way = same_as_previous + different_from_previous
            num_way_map[i] = num_way
        return num_way_map[n]
