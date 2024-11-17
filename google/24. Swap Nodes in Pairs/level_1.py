# 素直な解法
# 結構混乱した
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(None, head)
        node = sentinel
        while node.next and node.next.next:
            after = node.next
            before = node.next.next
            node.next = before
            after.next = before.next
            before.next = after
            node = node.next.next
        return sentinel.next
