class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        height = len(board)
        width = len(board[0])
        END_MARK = "$"
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[END_MARK] = word

        def back_tracking(row, col, parent):
            if (not 0 <= row < height) or (not 0 <= col < width):
                return
            if board[row][col] not in parent:
                return

            letter = board[row][col]
            node = parent[letter]

            if END_MARK in node:
                matched.append(node.pop(END_MARK))
            board[row][col] = "#"
            back_tracking(row - 1, col, node)
            back_tracking(row + 1, col, node)
            back_tracking(row, col - 1, node)
            back_tracking(row, col + 1, node)
            board[row][col] = letter

        matched = []
        for row in range(height):
            for col in range(width):
                if board[row][col] in root:
                    back_tracking(row, col, root)
        return matched
