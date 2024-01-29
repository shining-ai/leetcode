# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans_head = ListNode(0, head)
        ans = ans_head
        curr = head

        while curr != None:
            if curr.next != None and curr.val == curr.next.val:
                while curr.next != None and curr.val == curr.next.val:
                    curr = curr.next
                ans.next = curr.next
            else:
                ans = ans.next
            curr = curr.next

        return ans_head.next
