# DFSで実装
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        serial_tree = []

        def helper_serialize(node):
            if not node:
                serial_tree.append("null")
                return
            serial_tree.append(str(node.val))
            helper_serialize(node.left)
            helper_serialize(node.right)

        helper_serialize(root)
        return ",".join(serial_tree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper_deserialize(data):
            value = data.popleft()
            if value == "null":
                return None
            node = TreeNode(value)
            node.left = helper_deserialize(data)
            node.right = helper_deserialize(data)
            return node


        root = helper_deserialize(deque(data.split(",")))
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
