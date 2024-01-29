class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: ListNode) -> bool:
    node_seen = set()
    while head != None:
        if head in node_seen:
            return head
        node_seen.add(head)
        head = head.next

    return head


# O(n) time
# O(n) space
def hash_table(head: ListNode) -> bool:
    node_seen = set()
    while head != None:
        if head in node_seen:
            return head
        node_seen.add(head)
        head = head.next

    return head


if __name__ == "__main__":
    l = [3, 2, 0, -4]
    pos = 1

    dummy_head = ListNode(0)
    curr = dummy_head
    for i in l:
        node = ListNode(i)
        curr.next = node
        curr = node

    node = dummy_head.next
    for i in range(pos):
        node = node.next

    curr.next = node

    print(detectCycle(dummy_head.next))
    print(hash_table(dummy_head.next))
