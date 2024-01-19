# Definition for singly-linked list.
class SingleLinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"ListNode({self.val})"

    def __repr__(self):
        return f"ListNode({self.val})"

    def print_all_nodes(self):
        cur = self
        while cur:
            print(cur)
            cur = cur.next
