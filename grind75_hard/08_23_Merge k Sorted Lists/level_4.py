class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, node in enumerate(lists):
            if not node:
                continue
            # node.valが同値の場合にListNodeで比較しないようにindexをheapに追加
            heapq.heappush(min_heap, (node.val, i, node))
        sentinel = ListNode()
        node = sentinel
        while min_heap:
            val, index, smallest_head = heapq.heappop(min_heap)
            node.next = smallest_head
            node = node.next
            if smallest_head.next:
                heapq.heappush(
                    min_heap, (smallest_head.next.val, index, smallest_head.next)
                )
        return sentinel.next
