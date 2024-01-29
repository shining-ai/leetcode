class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# O(n) time, O(n) space
def set_val(head):
    if head == None:
        return None

    node_seen = set()
    node_seen.add(head.val)
    curr = head

    while curr.next != None:
        if curr.next.val in node_seen:
            curr.next = curr.next.next
        else:
            curr = curr.next
            node_seen.add(curr.val)

    return head


# O(n) time, O(1) space
def check_follow(head):
    curr = head

    while curr != None and curr.next != None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head


if __name__ == "__main__":
    l = [1, 1, 2]

    dummy_head = ListNode(0)
    curr = dummy_head
    for i in l:
        node = ListNode(i)
        curr.next = node
        curr = node

    ans = set_val(dummy_head.next)
    ans = check_follow(dummy_head.next)

    while ans != None:
        print(ans.val)
        ans = ans.next
