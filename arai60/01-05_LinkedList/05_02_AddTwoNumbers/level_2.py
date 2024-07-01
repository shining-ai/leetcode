# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sentinel = ListNode()
        node = sentinel
        carry = 0
        while l1 or l2 or carry:
            digit = carry
            if l1:
                digit += l1.val
                l1 = l1.next
            if l2:
                digit += l2.val
                l2 = l2.next
            carry = digit // 10
            digit = digit % 10
            node.next = ListNode(digit)
            node = node.next

        return sentinel.next
