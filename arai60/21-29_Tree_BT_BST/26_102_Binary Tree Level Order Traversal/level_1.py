class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


# O(n) time complexity
# O(n) space complexity
def solve_1(root):
    ans = []
    queue = collections.deque()
    queue.append((root, 0))

    while queue:
        node, level = queue.popleft()
        if not node:
            continue

        if len(ans) - 1 < level:
            ans.append([])

        ans[level].append(node.val)
        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))

    return ans


# Time complexity: O(n)
# Space complexity: O(n)
def solve_2(root, targetSum):
    if not root:
        return []

    ans = []

    def dfs(node, level):
        if len(ans) - 1 < level:
            ans.append([])

        ans[level].append(node.val)

        if node.left:
            dfs(node.left, level + 1)
        if node.right:
            dfs(node.right, level + 1)

    dfs(root, 0)

    return ans


if __name__ == "__main__":
    # root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(solve_1(root))
    # print(solve_2(root, targetSum))
