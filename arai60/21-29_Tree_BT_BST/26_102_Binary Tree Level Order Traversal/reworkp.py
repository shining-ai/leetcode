class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if not node:
                continue
            traversal[depth].append(node.val)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
        return list(traversal.values())
