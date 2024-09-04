# fixは確定しているものと考える。
# fix.nextにふさわしいかどうかを判定していく。
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        fix = sentinel
        while head and head.next:
            if head.val != head.next.val:
                fix = fix.next
                head = head.next
                continue
            val = head.val
            while head and head.val == val:
                head = head.next
            fix.next = head
        return sentinel.next


# nodeを直接編集する
# node.nextとnode.next.nextを比較することで、node.nextがふさわしいかどうかを判定していく。
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        node = sentinel
        while node and node.next and node.next.next:
            if node.next.val != node.next.next.val:
                node = node.next
                continue
            val = node.next.val
            while node.next and node.next.val == val:
                node.next = node.next.next
        return sentinel.next
