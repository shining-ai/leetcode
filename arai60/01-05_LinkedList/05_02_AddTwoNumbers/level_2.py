# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans_head = ListNode(0)
        ans = ans_head
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

            l_sum = v1 + v2 + carry
            carry = l_sum // 10
            new_val = l_sum % 10

            ans.next = ListNode(new_val)
            ans = ans.next

        return ans_head.next
