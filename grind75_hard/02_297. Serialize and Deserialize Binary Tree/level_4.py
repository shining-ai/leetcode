# NULL_SYMBOLを作成
# helper_deserializeの引数をイテレータに変更
# 変数名を修正
class Codec:
    NULL_SYMBOL = "#"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        serialized_tree = []

        def helper_serialize(node):
            if not node:
                serialized_tree.append(self.NULL_SYMBOL)
                return
            serialized_tree.append(str(node.val))
            helper_serialize(node.left)
            helper_serialize(node.right)

        helper_serialize(root)
        return ",".join(serialized_tree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper_deserialize(data):
            value = next(data)
            if value == self.NULL_SYMBOL:
                return None
            node = TreeNode(value)
            node.left = helper_deserialize(data)
            node.right = helper_deserialize(data)
            return node

        root = helper_deserialize(iter(data.split(",")))
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
