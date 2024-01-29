class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def check_follow(head):
    curr = head
    ans_head = ListNode(0, head)
    ans = ans_head

    while curr != None:
        if curr.next != None and curr.val == curr.next.val:
            while curr.next != None and curr.val == curr.next.val:
                curr = curr.next
            ans.next = curr.next
        else:
            ans = ans.next
        curr = curr.next

    return ans_head.next


if __name__ == "__main__":
    l = [1, 2, 3, 3, 4, 4, 5]

    dummy_head = ListNode(0)
    curr = dummy_head
    for i in l:
        node = ListNode(i)
        curr.next = node
        curr = node

    ans = check_follow(dummy_head.next)

    while ans != None:
        print(ans.val)
        ans = ans.next
