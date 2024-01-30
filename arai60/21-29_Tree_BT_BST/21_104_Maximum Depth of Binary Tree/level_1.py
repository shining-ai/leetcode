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
        return max(left_num, right_num)

    ans = dfs(root)
    return ans


# O(n) time
# O(n) space
def solve_2(root):
    if root is None:
        return 0

    stack = [(1, root)]
    ans = 0

    while stack:
        curr_depth, node = stack.pop()
        if node is not None:
            ans = max(ans, curr_depth)
            stack.append((curr_depth + 1, node.left))
            stack.append((curr_depth + 1, node.right))

    return ans


if __name__ == "__main__":
    # list_1 = [3, 9, 20, null, null, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    print(solve_1(root))
    print(solve_2(root))
