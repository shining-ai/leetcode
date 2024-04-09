# 問題文通りtableを作成して、k番目の値を返す(TLE)
# O(2^n)
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def build_table(table, n):
            if n == 0:
                return table
            new_table = ""
            for c in table:
                if c == "0":
                    new_table += "01"
                else:
                    new_table += "10"
            return build_table(new_table, n - 1)

        table = build_table("0", n - 1)
        return int(table[k - 1])


# 1  0
# 2  01
# 3  0110
# 4  01101001
# 1つ前のテーブルを反転させたものが後ろにくっつく性質を利用
# 例えば4つ目のテーブルは、(0110) + (0110の反転)となる
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        total_element = 2 ** (n - 1)
        half_element = total_element // 2
        if half_element < k:
            return 1 - self.kthGrammar(n - 1, k - half_element)
        return self.kthGrammar(n - 1, k)
