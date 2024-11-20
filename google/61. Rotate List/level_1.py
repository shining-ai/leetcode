# 素直に解く
# 1. リストの長さを求める
# 2. 新しいしっぽを見つける
# 3. 新しいしっぽの次のノードを新しいヘッドにする
# 例外を考慮する
# 1. リストが空の場合
# 2. リストの長さが1の場合
# 3. kがリストの長さで割り切れる場合(回転しない場合)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        sentinel = ListNode(None, head)
        node = head
        node_length = 0
        while node:
            node_length += 1
            node = node.next
        if node_length == 1:
            return head
        if k % node_length == 0:
            return head

        node = sentinel
        tail = sentinel
        for _ in range((k % node_length) + 1):
            node = node.next
        while node:
            node = node.next
            tail = tail.next
        sentinel.next = tail.next
        next_head = tail.next
        while next_head and next_head.next:
            next_head = next_head.next
        next_head.next = head
        tail.next = None

        return sentinel.next
