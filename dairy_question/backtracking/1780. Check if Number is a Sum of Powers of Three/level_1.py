class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        def helper(next_i, remain):
            if remain == 0:
                return True
            if remain < 0:
                return False
            for i in range(next_i, 20):
                if helper(i + 1, remain - 3 ** i):
                    return True
            return False
        return helper(0, n)
