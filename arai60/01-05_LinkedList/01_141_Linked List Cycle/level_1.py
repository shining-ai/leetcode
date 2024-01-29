class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# O(n) time
# O(n) space
def hash_table(head: ListNode) -> bool:
    node_seen = set()

    while head != None:
        if head in node_seen:
            return True
        node_seen.add(head)
        head = head.next

    return False


# O(n) time
# O(1) space
def FloydsCycleFinding(head: ListNode) -> bool:
    if head == None:
        return False

    slow = head
    fast = head.next
    while slow != fast:
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


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

    print(hash_table(dummy_head.next))
    print(FloydsCycleFinding(dummy_head.next))
