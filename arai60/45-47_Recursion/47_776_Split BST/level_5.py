# stackを使った解法
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        stack = [("go", root, None)]
        while stack:
            go_back_flag, node, direction = stack.pop()
            if go_back_flag == "go":
                if not node:
                    smaller_child = None
                    greater_child = None
                    continue
                if node.val <= target:
                    stack.append(("back", node, "right"))
                    stack.append(("go", node.right, None))
                else:
                    stack.append(("back", node, "left"))
                    stack.append(("go", node.left, None))
            if go_back_flag == "back":
                if direction == "left":
                    node.left = smaller_child
                    smaller_child = node
                else:
                    node.right = greater_child
                    greater_child = node
        return greater_child, smaller_child

