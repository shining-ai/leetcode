# BFSで実装
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        serial_tree = []
        node_queue = deque([root])
        while node_queue:
            node = node_queue.popleft()
            if not node:
                serial_tree.append("null")
                continue
            serial_tree.append(str(node.val))
            node_queue.append(node.left)
            node_queue.append(node.right)
        return ",".join(serial_tree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data_queue = deque(list(data.split(",")))
        value = data_queue.popleft()
        root = TreeNode(value)
        node_queue = deque([root])
        while data_queue:
            left_value = data_queue.popleft()
            right_value = data_queue.popleft()
            node = node_queue.popleft()
            if not left_value == "null":
                node.left = TreeNode(left_value)
                node_queue.append(node.left)
            if not right_value == "null":
                node.right = TreeNode(right_value)
                node_queue.append(node.right)
        return root
