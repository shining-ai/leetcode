# 実直に解く
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        sentinel = ListNode(None, head)
        node = sentinel
        reversed_list = None
        current = 1
        while current < left:
            node = node.next
            current += 1
        pre_list_tail = node
        node = node.next
        reversed_tail = node
        while current <= right:
            remain_head = node.next
            node.next = reversed_list
            reversed_list = node
            node = remain_head
            current += 1
        if node:
            reversed_tail.next = remain_head
        pre_list_tail.next = reversed_list
        return sentinel.next
