MOD = 10**9 + 7
MAXN = 10**5

# 階乗とその逆元のテーブル
factorial = [0] * MAXN
inv_factorial = [0] * MAXN


# 高速べき乗
def mod_pow(base, exp):
    result = 1
    while exp:
        if exp & 1:
            result = result * base % MOD
        base = base * base % MOD
        exp >>= 1
    return result


# 階乗と逆元を初期化
def precompute_factorials():
    if factorial[0] != 0:
        return
    factorial[0] = 1
    for i in range(1, MAXN):
        factorial[i] = factorial[i - 1] * i % MOD
    inv_factorial[MAXN - 1] = mod_pow(factorial[MAXN - 1], MOD - 2)
    for i in range(MAXN - 1, 0, -1):
        inv_factorial[i - 1] = inv_factorial[i] * i % MOD


# 組み合わせ (nCk) を計算
def comb(n, k):
    if k < 0 or k > n:
        return 0
    return factorial[n] * inv_factorial[k] % MOD * inv_factorial[n - k] % MOD


# メイン処理
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        precompute_factorials()

        total_ways = m # array[0]の組み合わせ
        total_ways = total_ways * comb(n - 1, k) % MOD # 前の要素と同じになるindexの組み合わせ
        total_ways = total_ways * mod_pow(m - 1, n - 1 - k) % MOD # 前の要素と異なる部分の組み合わせ
        return total_ways
