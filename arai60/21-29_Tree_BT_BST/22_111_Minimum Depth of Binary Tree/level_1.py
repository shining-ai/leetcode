class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time
# O(n) space
def solve_1(root):
    def dfs(root):
        if root is None:
            return 0

        left_num = dfs(root.left) + 1
        right_num = dfs(root.right) + 1

        if left_num == 1 or right_num == 1:
            return max(left_num, right_num)
        return min(left_num, right_num)

    ans = dfs(root)
    return ans


import collections


# O(n) time
# O(n) space
def solve_2(root):
    if root is None:
        return 0

    queue = collections.deque()
    queue.append((root, 1))

    while queue:
        node, depth = queue.popleft()
        if node.left is None and node.right is None:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))


if __name__ == "__main__":
    # list_1 = [3, 9, 20, null, null, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    print(solve_1(root))
    print(solve_2(root))
