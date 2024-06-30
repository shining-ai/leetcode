class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        half_element = 2 ** (n - 1)
        if half_element < k:
            return 1 - self.kthGrammar(n - 1, k - half_element)
        return self.kthGrammar(n - 1, k)
