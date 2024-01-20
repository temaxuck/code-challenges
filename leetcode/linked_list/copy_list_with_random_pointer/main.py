from typing import Optional
from linked_list import RandomLinkedListNode as ListNode


class Solution:
    def copyRandomList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur1 = head  # original
        cur2 = head  # copy

        while cur1:
            cur1.next = ListNode(cur1.val, cur1.next)
            cur1 = cur1.next.next

        while cur2:
            cur2.next.random = cur2.random.next if cur2.random else None
            cur2 = cur2.next.next

        cur1 = head
        cur2 = new_head = head.next

        while cur2:
            cur1.next = cur1.next.next
            if cur2.next:
                cur2.next = cur2.next.next
            else:
                break
            cur1 = cur1.next
            cur2 = cur2.next

        return new_head


l = ListNode(7)
l.next = ListNode(13)
l.next.next = ListNode(11)
l.next.next.next = ListNode(10)
l.next.next.next.next = ListNode(1)
l.random = None
l.next.random = l
l.next.next.random = l.next.next.next.next
l.next.next.next.random = l.next.next
l.next.next.next.next.random = l
Solution().copyRandomList(l).print_all_nodes()
