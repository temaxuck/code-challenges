from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}"

    def __repr__(self):
        return f"{self.val}"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        current = head

        while current:
            next_node = current.next
            current.next = node
            node = current
            current = next_node

        return node


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
print(Solution().reverseList(l))
