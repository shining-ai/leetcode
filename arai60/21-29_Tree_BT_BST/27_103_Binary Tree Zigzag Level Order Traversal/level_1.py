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

    for i in range(len(ans)):
        if i % 2 != 0:
            ans[i].reverse()
    return ans


def solve_2(root):
    ans = []
    queue = collections.deque()
    queue.append((root, 0))

    while queue:
        node, level = queue.popleft()
        if not node:
            continue

        if len(ans) - 1 < level:
            ans.append([])

        if level % 2 != 0:
            ans[level].insert(0, node.val)
        else:
            ans[level].append(node.val)

        queue.appendleft((node.right, level + 1))
        queue.appendleft((node.left, level + 1))

    return ans


def solve_3(root):
    ans = []

    def dfs(node, level):
        if not node:
            return

        if len(ans) - 1 < level:
            ans.append([])

        if level % 2 != 0:
            ans[level].insert(0, node.val)
        else:
            ans[level].append(node.val)

        dfs(node.left, level + 1)
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
    print(solve_2(root))
