class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head: ListNode) -> bool:
    prev = None

    while head != None:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev


if __name__ == "__main__":
    l = [3, 2, 0, -4]
    pos = 1

    dummy_head = ListNode(0)
    curr = dummy_head
    for i in l:
        node = ListNode(i)
        curr.next = node
        curr = node

    ans = reverse_list(dummy_head.next)
    while ans != None:
        print(ans.val)
        ans = ans.next
