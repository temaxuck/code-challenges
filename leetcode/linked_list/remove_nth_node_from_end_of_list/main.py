from typing import Optional
from linked_list import SingleLinkedListNode as ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next

        nodes_len = len(nodes)
        cur = new_head = ListNode()

        for i, node in enumerate(nodes):
            if i == nodes_len - n:
                continue

            cur.next = node
            cur = cur.next

        cur.next = None

        return new_head.next


l = ListNode(1)
# l.next = ListNode(2)
# l.next.next = ListNode(3)
# l.next.next.next = ListNode(4)
# l.next.next.next.next = ListNode(5)
Solution().removeNthFromEnd(l, 1).print_all_nodes()
