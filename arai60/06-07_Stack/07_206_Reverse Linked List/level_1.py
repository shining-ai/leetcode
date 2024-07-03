# 実直な解法
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        node = head
        prev_node = None
        while node:
            next_node = node.next
            node.next = prev_node
            sentinel.next = node
            prev_node = node
            node = next_node
        return sentinel.next


# 再帰を使った解法1
# リストの接続は呼び出し先の関数にやってもらう
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(node):
            if not node.next:
                return node, node
            reversed_head, reversed_tail = reverse_list_helper(node.next)
            node.next = None
            reversed_tail.next = node
            return reversed_head, reversed_tail.next

        if not head:
            return None
        head, tail = reverse_list_helper(head)
        return head


# 再帰を使った解法2
# リストの接続をやってから次の関数に渡す
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(reversed, rest):
            if not rest:
                return reversed
            rest_head = rest.next
            reversed_tail = reversed
            ans = rest
            ans.next = reversed_tail
            ans = reverse_list_helper(ans, rest_head)
            return ans

        return reverse_list_helper(None, head)
