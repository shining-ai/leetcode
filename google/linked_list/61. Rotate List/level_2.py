# 循環リストにして、新しい尻尾で切断する
# 1. リストの長さを求める
# 2. 新しいしっぽを見つける
# 3. 新しいしっぽの次のノードを新しいヘッドにする
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        tail = head
        node_length = 1
        while tail.next:
            node_length += 1
            tail = tail.next
        tail.next = head
        new_tail = head
        for _ in range(node_length - k % node_length - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        return new_head
