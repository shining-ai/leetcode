# 単純な解法
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = None
        while head:
            next_head = head.next
            head.next = reversed_list
            reversed_list = head
            head = next_head
        return reversed_list


# 再帰
# 先頭と末尾が返ってくれば、作業ができると考える
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if not node:
                return None, None
            if not node.next:
                return node, node
            head, tail = helper(node.next)
            node.next = None
            tail.next = node
            tail = tail.next
            return head, tail

        reversed_list, _ = helper(head)
        return reversed_list


# 再帰
# ひっくり返ったものを返してもらう
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(reverse_list, rest):
            if not rest:
                return reverse_list
            rest_head = rest.next
            rest.next = reverse_list
            return helper(rest, rest_head)

        return helper(None, head)
