from typing import Optional, List
from trees import BinaryTreeNode as TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [(root, 1)]
        res = []

        while stack:
            node, level = stack.pop()

            if len(res) < level:
                res.append(node.val)
            else:
                res[level - 1] = node.val

            if node.right:
                stack.append((node.right, level + 1))

            if node.left:
                stack.append((node.left, level + 1))

        return res


# # passed
# root = TreeNode(6)
# root.left = TreeNode(2)
# root.right = TreeNode(8)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(7)
# root.left.right.left = TreeNode(3)
# print(Solution().rightSideView(root))

# passed
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(Solution().rightSideView(root))
