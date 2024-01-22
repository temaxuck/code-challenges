from typing import Optional, List
from trees import BinaryTreeNode as TreeNode
from collections import deque


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        stack = [(preorder, inorder, idx, root)]

        while stack:
            pre, ino, idx, node = stack.pop()

            if not pre:
                continue

            l, r = 1 if idx > 0 else None, idx + 1 if idx + 1 < len(pre) else None

            if l is not None:
                next_node = node.left = TreeNode(pre[l])
                next_pre, next_ino = pre[1 : idx + 1], ino[:idx]
                next_idx = next_ino.index(pre[l])
                stack.append((next_pre, next_ino, next_idx, next_node))
                # stack.append((pre[1:next_idx+1]))

            if r is not None:
                next_node = node.right = TreeNode(pre[r])
                next_pre, next_ino = pre[idx + 1 :], ino[idx + 1 :]
                next_idx = next_ino.index(pre[r])
                stack.append((next_pre, next_ino, next_idx, next_node))

        return root


# passed
# tree = Solution().buildTree([1, 2, 4, 7, 9, 5, 3, 6, 8], [7, 9, 4, 2, 5, 1, 3, 6, 8])
# print(tree.right.left, tree.right.right.right)

tree = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
tree.print_all_nodes()
# print(tree.right.left, tree.right.right.right)
