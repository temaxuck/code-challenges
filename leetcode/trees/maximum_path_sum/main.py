from typing import Optional
from trees import BinaryTreeNode as TreeNode
from collections import deque

"""
My attempt at solving this problem (Failed)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        dq = deque([(root, [root])])
        paths = deque([])

        while dq:
            node, path = dq.popleft()
            paths.append(path)

            # max_sum = max(current_sum, max_sum)

            # print(current_sum, node)
            # if stack:
            #     neighbour, neighbour_parent, neighbour_current_sum = stack[-1]
            #     if parent == neighbour_parent:
            #         stack[-1] = (
            #             neighbour,
            #             neighbour_parent,
            #             neighbour_current_sum + node.val,
            #         )

            if node.left:
                dq.append((node.left, [*path, *[node.left]]))

            if node.right:
                dq.append((node.right, [*path, *[node.right]]))

            if node.left and node.right:
                # leaf_paths = []
                # cur1 = node.left
                # while cur1:
                #     if cur1.left:
                #         dq.append((cur1.left, [cur1.left, cur1, node]))
                #     if cur1.right:
                #         dq.append((cur1.right, [cur1.right, cur1, node]))
                #     cur = cur.left
                dq.append((node.left, [node.left, node, node.right]))
                dq.append((node.right, [node.left, node, node.right]))

        print(paths)

        # for path in paths:
        #     if
        # prev_path = None
        # stack = [paths.popleft()]

        while paths:
            path = paths.popleft()
            current_sum = sum(node.val for node in path)
            max_sum = max(max_sum, current_sum)
            print(current_sum, path)

        return max_sum
"""


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def get_max_gain(root):
            nonlocal max_sum

            if not root:
                return 0

            left_gain = max(get_max_gain(root.left), 0)
            right_gain = max(get_max_gain(root.right), 0)

            max_sum = max(max_sum, left_gain + root.val + right_gain)

            return root.val + max(left_gain, right_gain)

        get_max_gain(root)

        return max_sum


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# print(Solution().maxPathSum(root))
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right.right = TreeNode(4)
print(Solution().maxPathSum(root))
