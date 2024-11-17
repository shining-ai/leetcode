# 率直な解法
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_num = 0
        node = head
        while node:
            list_num += 1
            node = node.next
        sentinel = ListNode(None, head)
        node = sentinel
        for i in range(list_num - n):
            node = node.next
        node.next = node.next.next
        return sentinel.next


# 率直な解法を再帰で書いてみる
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(node):
            if not node:
                return 1, None
            num, next_node = helper(node.next)
            if num == n:
                return num + 1, next_node
            node.next = next_node
            return num + 1, node

        _, node = helper(head)
        return node


# ポインターを2つ使う解法
# 2つのポインターをnずらしておけば、片方が末尾に到達したときにもう片方が末尾からn番目になる
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(None, head)
        node_1 = sentinel
        node_2 = sentinel
        for _ in range(n + 1):
            node_1 = node_1.next
        while node_1:
            node_1 = node_1.next
            node_2 = node_2.next
        node_2.next = node_2.next.next
        return sentinel.next
