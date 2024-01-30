class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


def solve_1(root):
    if not root:
        return True

    stack = [(root, -float("inf"), float("inf"))]

    while stack:
        node, low, high = stack.pop()
        if not node:
            continue
        if not (low < node.val < high):
            return False
        stack.append((node.right, node.val, high))
        stack.append((node.left, low, node.val))

    return True


def solve_2(root):
    def valid_tree_dfs(node, low=-float("inf"), high=float("inf")):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return valid_tree_dfs(node.right, node.val, high) and valid_tree_dfs(
            node.left, low, node.val
        )

    return valid_tree_dfs(root)


if __name__ == "__main__":
    # root = [32,26,47,19,null,null,56,null,27]
    root = TreeNode(32)
    root.left = TreeNode(26)
    root.right = TreeNode(47)
    root.left.left = TreeNode(19)
    root.right.right = TreeNode(56)
    root.left.left.right = TreeNode(27)

    print(solve_1(root))
    print(solve_2(root))
