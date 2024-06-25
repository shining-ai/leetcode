class Solution:

    def reverse_list(self, head, joined_head, k):
        new_head = joined_head
        current = head
        for _ in range(k):
            next_node = current.next
            current.next = new_head
            new_head = current
            current = next_node
        return new_head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            count += 1
            if count == k:
                break
            current = current.next
        if count != k:
            return head

        joined_head = current.next
        joined_head = self.reverseKGroup(joined_head, k)
        new_head = self.reverse_list(head, joined_head, k)
        return new_head
