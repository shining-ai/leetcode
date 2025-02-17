class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = defaultdict(int)
        for tile in tiles:
            counts[tile] += 1

        possible_num = 0

        def helper():
            nonlocal possible_num
            for key in counts:
                if counts[key] <= 0:
                    continue
                counts[key] -= 1
                possible_num += 1
                helper()
                counts[key] += 1

        helper()
        return possible_num
