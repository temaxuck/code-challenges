from typing import Optional, List
from trees import BinaryTreeNode as TreeNode
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dq = deque([(root, 1)])
        max_level = 0
        nodes = []

        while dq:
            node, level = dq.popleft()
            nodes.append((node.val, level))
            max_level = max(max_level, level)

            if node.left:
                dq.append((node.left, level + 1))

            if node.right:
                dq.append((node.right, level + 1))

        res = []
        i = 0
        n = len(nodes)
        current_level = 1

        while current_level <= max_level:
            tmp = []
            while i < n and nodes[i][1] == current_level:
                tmp.append(nodes[i][0])
                i += 1
            res.append(tmp)
            current_level += 1

        return res


# # passed
# root = TreeNode(6)
# root.left = TreeNode(2)
# root.right = TreeNode(8)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(7)
# root.right.right = TreeNode(9)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)
# print(Solution().levelOrder(root))

# passed
# root = TreeNode(6)
# root.left = TreeNode(2)
# root.left.left = TreeNode(0)
# root.left.left.left = TreeNode(3)
# root.left.left.left.left = TreeNode(11)
# print(Solution().levelOrder(root))
