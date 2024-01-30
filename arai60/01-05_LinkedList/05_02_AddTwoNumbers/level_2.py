# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sentinel = ListNode(0)
        current = sentinel
        carry = 0
        while l1 or l2 or carry:
            v1 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            v2 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            current_val = v1 + v2 + carry
            carry = current_val // 10
            current_digit = current_val % 10
            current.next = ListNode(current_digit)
            current = current.next
        return sentinel.next
