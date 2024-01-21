from typing import Optional
from trees import BinaryTreeNode as TreeNode
from collections import deque


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        stack1 = []
        stack2 = []
        cur1 = cur2 = root

        while cur1 or cur2:
            if cur1:
                if p.val == cur1.val:
                    cur1 = None
                elif p.val < cur1.val:
                    stack1.append(cur1)
                    cur1 = cur1.left
                elif p.val > cur1.val:
                    stack1.append(cur1)
                    cur1 = cur1.right
            if cur2:
                if q.val == cur2.val:
                    cur2 = None
                elif q.val < cur2.val:
                    stack2.append(cur2)
                    cur2 = cur2.left
                elif q.val > cur2.val:
                    stack2.append(cur2)
                    cur2 = cur2.right

        common_ancestor = root

        while stack1 and stack2:
            if len(stack1) < len(stack2):
                node = stack2.pop()

                if node.val == p.val:
                    return node

                continue

            if len(stack1) > len(stack2):
                node = stack1.pop()

                if node.val == q.val:
                    return node

                continue

            if len(stack1) == len(stack2):
                node1 = stack1.pop()
                node2 = stack2.pop()

                if node1 == node2:
                    common_ancestor = node1
                    break

        return common_ancestor


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.print_all_nodes()
print("-" * 40)
print(Solution().lowestCommonAncestor(root, root.left, root.left.right))
