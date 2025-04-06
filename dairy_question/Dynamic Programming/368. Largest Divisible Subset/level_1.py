class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subsets = {-1: set()}

        # nums を昇順にソートして、小さい順に処理
        for num in sorted(nums):
            max_subset = set()

            # 今までの subsets を全部見て、自分（num）で割り切れるものだけを対象にする
            for k in subsets:
                if num % k == 0:
                    if len(subsets[k]) > len(max_subset):
                        max_subset = subsets[k]

            # 一番長かった部分集合に num を加えて新しい部分集合を作る
            subsets[num] = max_subset | {num}

        # 最終的に subsets の中で一番長い集合を取り出してリストに変換して返す
        result = []
        for subset in subsets.values():
            if len(subset) > len(result):
                result = list(subset)

        return result
