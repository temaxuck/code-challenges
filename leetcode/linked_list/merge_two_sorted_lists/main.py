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

    def print_all_nodes(self):
        cur = self
        while cur:
            print(cur)
            cur = cur.next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # res = min(list1, list2, key=lambda x: x.val)
        cur1 = list1
        cur2 = list2

        if not cur1 and not cur2:
            return None

        if not cur1:
            return cur2

        if not cur2:
            return cur1

        if cur1.val > cur2.val:
            res = cur2
            cur2 = cur2.next
        else:
            res = cur1
            cur1 = cur1.next

        cur = res

        while True:
            if not cur1 and not cur2:
                break

            if not cur1:
                cur.next = cur2
                break

            if not cur2:
                cur.next = cur1
                break

            if cur1.val > cur2.val:
                cur.next = cur2
                cur2 = cur2.next
            else:
                cur.next = cur1
                cur1 = cur1.next

            cur = cur.next

        return res

        # res = ListNode()

        # while cur1:
        #     next1 = cur1.next
        #     next2 = cur2.next

        #     if cur1.next > cur2.next:
        #         res =


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
Solution().mergeTwoLists(l1, l2).print_all_nodes()
