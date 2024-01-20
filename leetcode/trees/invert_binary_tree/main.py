from typing import Optional
from trees import BinaryTreeNode as TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()

            l, r = node.left, node.right
            node.left, node.right = r, l

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
root.print_all_nodes()
print("-" * 20)
Solution().invertTree(root).print_all_nodes()
