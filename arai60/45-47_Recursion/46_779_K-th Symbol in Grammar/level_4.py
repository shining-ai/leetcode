# int.bit_count()を使用
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return (k - 1).bit_count() % 2


# 変数名が分かりづらいので修正
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        # n row の要素数は2 ** (n - 1)
        num_half_elements = 2 ** (n - 2)
        if num_half_elements < k:
            return 1 - self.kthGrammar(n - 1, k - num_half_elements)
        return self.kthGrammar(n - 1, k)
