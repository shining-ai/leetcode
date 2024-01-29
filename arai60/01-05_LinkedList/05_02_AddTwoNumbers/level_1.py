class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def AddTwoNumbers(l1, l2):
    ans_head = ListNode(0)
    ans = ans_head
    carry = 0

    while l1 or l2 or carry:
        v1 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next

        v2 = 0
        if l2:
            v2 = l2.val
            l2 = l2.next

        l_sum = v1 + v2 + carry
        carry = l_sum // 10
        new_val = l_sum % 10

        ans.next = ListNode(new_val)
        ans = ans.next

    return ans_head.next


if __name__ == "__main__":
    l1_1 = ListNode(3)
    l1_2 = ListNode(4, l1_1)
    l1_3 = ListNode(2, l1_2)
    l1 = l1_3

    l2_1 = ListNode(4)
    l2_2 = ListNode(6, l2_1)
    l2_3 = ListNode(5, l2_2)
    l2 = l2_3

    AddTwoNumbers(l1, l2)
