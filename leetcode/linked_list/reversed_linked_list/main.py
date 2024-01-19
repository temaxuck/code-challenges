from typing import Optional
from linked_list import SingleLinkedListNode as ListNode


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
