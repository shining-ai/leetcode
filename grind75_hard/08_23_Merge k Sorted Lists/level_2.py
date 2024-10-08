# heapqに先頭の値だけを入れていく
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, node in enumerate(lists):
            if not node:
                continue
            heapq.heappush(min_heap, (node.val, i, node))
        sentinel = ListNode()
        node = sentinel
        while min_heap:
            val, index, smallest_head = heapq.heappop(min_heap)
            node.next = ListNode(val)
            node = node.next
            if smallest_head.next:
                heapq.heappush(
                    min_heap, (smallest_head.next.val, index, smallest_head.next)
                )
        return sentinel.next
