from typing import Optional
from trees import BinaryTreeNode as TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 0

        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.left:
                stack.append((node.left, depth + 1))

            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.print_all_nodes()
print(Solution().maxDepth(root))
