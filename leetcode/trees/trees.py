from collections import deque


# Definition for singly-linked list.
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"BinaryTreeNode({self.val})"

    def __repr__(self):
        return f"BinaryTreeNode({self.val})"

    def print_all_nodes(self):
        dq = deque([self])

        while dq:
            node = dq.popleft()
            print(node)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
