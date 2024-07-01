# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        dupulication_node = sentinel
        node = head
        while node:
            if not node.next or node.val != node.next.val:
                dupulication_node.next = node
                dupulication_node = dupulication_node.next
            while node.next and node.val == node.next.val:
                node = node.next
            node = node.next
        dupulication_node.next = node

        return sentinel.next
