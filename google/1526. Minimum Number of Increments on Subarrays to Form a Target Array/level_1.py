# 左から順に見ていって、昇順の場合は最大値がそこまでの回数と同じになる
# 1 2 4 2 3
# 左の1 2 3 は4回の操作で消せる
# 右の2 3 の塊は、差分の1回で消せる

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev_value = 0
        count = 0
        for i in range(len(target)):
            if target[i] - prev_value > 0:
                count += target[i] - prev_value
            prev_value = target[i]
        return count
