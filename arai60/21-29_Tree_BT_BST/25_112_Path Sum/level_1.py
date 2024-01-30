class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(n)
def solve_1(root, targetSum):
    if not root:
        return False

    ans = False
    sum = 0

    def dfs(root, sum):
        nonlocal ans
        if not root:
            return None

        sum += root.val
        if not root.left and not root.right:
            if sum == targetSum:
                ans = True
            return None

        dfs(root.left, sum)
        dfs(root.right, sum)

    dfs(root, sum)
    return ans


import collections


# Time complexity: O(n)
# Space complexity: O(n)
def solve_2(root, targetSum):
    if not root:
        return False

    queue = []
    queue.append((root, root.val))

    while queue:
        node, sum = queue.pop()
        if not node.left and not node.right:
            if sum == targetSum:
                return True

        if node.left:
            queue.append((node.left, sum + node.left.val))
        if node.right:
            queue.append((node.right, sum + node.right.val))

    return False


if __name__ == "__main__":
    # [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    # root.left.right = TreeNode(None)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    # root.right.left.left = TreeNode(None)
    # root.right.left.right = TreeNode(None)
    # root.right.right.left = TreeNode(None)
    root.right.right.right = TreeNode(1)
    targetSum = 22

    print(solve_1(root, targetSum))
    print(solve_2(root, targetSum))
