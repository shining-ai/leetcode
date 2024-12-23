# 要素を全て入れて、sortしてからlinked listに変換
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists_val = []
        for node in lists:
            while node:
                lists_val.append(node.val)
                node = node.next
        lists_val.sort()
        sentinel = ListNode()
        node = sentinel
        for i in lists_val:
            node.next = ListNode(i)
            node = node.next

        return sentinel.next


# 各linked listの先頭を比較していく
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentinel = ListNode()
        node = sentinel
        while lists:
            min_val = float("inf")
            for i in range(len(lists)):
                if not lists[i] or lists[i].val > min_val:
                    continue
                min_val = lists[i].val
                min_index = i
            if min_val == float("inf"):
                break
            node.next = ListNode(min_val)
            node = node.next
            min_node = lists.pop(min_index)
            min_node = min_node.next
            if min_node:
                lists.append(min_node)

        return sentinel.next
