# バックトラッキングで全パターン試していく
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []

        def make_happy_string(current):
            if len(happy_strings) >= k:
                return True
            if len(current) == n:
                happy_strings.append(current[:])
                return False
            for letter in ["a", "b", "c"]:
                if current and current[-1] == letter:
                    continue
                current.append(letter)
                if make_happy_string(current):
                    return True
                current.pop()
            return False

        make_happy_string([])
        if len(happy_strings) < k:
            return ""
        return "".join(happy_strings[k-1])
