class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i, brank in enumerate(s):
            if brank == "(":
                stack.append(i)
                continue
            stack.pop()
            if not stack:
                stack.append(i)
                continue
            length = i - stack[-1]
            max_length = max(max_length, length)

        return max_length
