class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)

        prev_row = [str2[0:col] for col in range(str2_length + 1)]
        for row in range(1, str1_length + 1):
            curr_row = [str1[0:row]] + [None for _ in range(str2_length)]
            for col in range(1, str2_length + 1):
                if str1[row - 1] == str2[col - 1]:
                    curr_row[col] = prev_row[col - 1] + str1[row - 1]
                else:
                    pick_s1 = prev_row[col]
                    pick_s2 = curr_row[col - 1]
                    curr_row[col] = (
                        pick_s1 + str1[row - 1]
                        if len(pick_s1) < len(pick_s2)
                        else pick_s2 + str2[col - 1]
                    )
            prev_row = curr_row
        return prev_row[str2_length]
