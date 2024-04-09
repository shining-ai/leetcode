# level_1と同じ解法
# 余計な変数(total_element)を削除
# 再帰の終了をkで判定するように修正
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        # n row の要素数は2 ** (n - 1)
        half_element = 2 ** (n - 2)
        if half_element < k:
            return 1 - self.kthGrammar(n - 1, k - half_element)
        return self.kthGrammar(n - 1, k)


# 数学的な解法
# ↑のコードから、反転する回数(kを2進数で表した時の1が立つビット)だけわかれば良い
# 01101001
# 3 0110 2回反転
# 4 1000 1回反転
# 5 1001 2回反転
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count("1") % 2
