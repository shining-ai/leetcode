# Brute Force(TLE)
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        num = 0
        for i in range(-k + 1, len(colors) - k + 1):
            prev_color = None
            current = i
            current_list = colors[current: current + k]
            while current < i + k:
                if colors[current] == prev_color:
                    break
                prev_color = colors[current]
                current += 1
            else:
                num += 1
        return num


# Sliding Window
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        start = -k + 1
        end = -k + 1
        num_alternating = 0
        prev_last_color = None
        while end < len(colors):
            if prev_last_color == colors[end]:
                start = end
            if end - start + 1 == k:
                num_alternating += 1
                start += 1
            prev_last_color = colors[end]
            end += 1
        return num_alternating
