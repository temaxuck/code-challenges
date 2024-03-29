from typing import Optional
from linked_list import SingleLinkedListNode as ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l, r = head, head

        while r and r.next:
            l = l.next
            r = r.next.next

        reversed_node = None
        cur = l

        while cur:
            next_node = cur.next
            cur.next = reversed_node
            reversed_node = cur
            cur = next_node

        cur1 = head
        cur2 = reversed_node

        while True:
            if not cur2:
                break
            next1, next2 = cur1.next, cur2.next

            cur1.next, cur2.next = cur2, next1
            cur1, cur2 = next1, next2

        if cur1:
            cur1.next = None


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
# l.next.next.next.next.next = ListNode(6)
Solution().reorderList(l)
l.print_all_nodes()
