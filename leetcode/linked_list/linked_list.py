import secrets


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


class RandomLinkedListNode(SingleLinkedListNode):
    def __init__(
        self,
        x: int = 0,
        next: SingleLinkedListNode = None,
        random: SingleLinkedListNode = None,
    ):
        self.val = int(x)
        self.next = next
        self.random = random
        self.hash = secrets.token_hex(4)

    def print_all_nodes(self):
        cur = self
        while cur:
            if cur.random:
                print(
                    f"{cur} ({cur.hash}) --Random-Link--> {cur.random} ({cur.random.hash})"
                )
            else:
                print(f"{cur} ({cur.hash}) --Random-Link--> None")
            cur = cur.next
