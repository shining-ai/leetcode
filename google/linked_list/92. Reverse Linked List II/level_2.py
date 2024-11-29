# イテレーティブに解く
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        sentinel = ListNode(None, head)
        connect_left = sentinel
        current = 1
        while current < left:
            connect_left = connect_left.next
            current += 1
        remain_head = connect_left.next
        reversed_tail = remain_head
        reversed_list = None
        while current <= right:
            next_remain = remain_head.next
            remain_head.next = reversed_list
            reversed_list = remain_head
            remain_head = next_remain
            current += 1
        if remain_head:
            reversed_tail.next = remain_head
        connect_left.next = reversed_list
        return sentinel.next
