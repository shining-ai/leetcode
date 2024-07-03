# 実直な解法
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev


# 再帰を使った解法1
# リストの接続は呼び出し先の関数にやってもらう
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(node):
            if not node:
                return None
            if not node.next:
                return node
            head = reverse_list_helper(node.next)
            node.next.next = node  # reverse_listのtailはnode.next
            node.next = None
            return head

        return reverse_list_helper(head)


# 再帰を使った解法2
# リストの接続をやってから次の関数に渡す
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(reversed, rest):
            if not rest:
                return reversed
            remain = rest.next
            rest.next = reversed
            rest = reverse_list_helper(rest, remain)
            return rest

        return reverse_list_helper(None, head)
