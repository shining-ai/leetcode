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


# マージソートをイメージした解法
# 先頭の2つのリストをマージしていき、最後の1つになるまで繰り返す
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(list_1, list_2):
            sentinel = ListNode()
            node = sentinel
            while list_1 and list_2:
                if list_1.val < list_2.val:
                    node.next = list_1
                    list_1 = list_1.next
                else:
                    node.next = list_2
                    list_2 = list_2.next
                node = node.next
            if not list_1:
                node.next = list_2
            else:
                node.next = list_1
            return sentinel.next

        list_queue = deque(lists)
        if not list_queue:
            return None
        while 1:
            list_1 = list_queue.popleft()
            if not list_queue:
                return list_1
            list_2 = list_queue.popleft()
            mearged_list = merge_two_lists(list_1, list_2)
            list_queue.append(mearged_list)
