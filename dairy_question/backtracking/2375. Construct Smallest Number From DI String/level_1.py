# バックトラッキングで試していく
# patternのインデックスのズレがうまく解消できずに同じ条件がループ内に残ってしまった。
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = [0] * 10
        current = []

        def helper(index, small, big):
            nonlocal current
            if len(current) == len(pattern) + 1:
                return True
            for i in range(small, big):
                if used[i] == 1:
                    continue
                used[i] = 1
                current.append(i)
                if len(current) == len(pattern) + 1:
                    return True

                if pattern[index] == "I":
                    left = i + 1
                    right = 10
                else:
                    left = 1
                    right = i
                if helper(index + 1, left, right):
                    return True
                current.pop()
                used[i] = 0

        helper(0, 1, 10)
        return "".join(map(str, current))
