from typing import Optional
from graphs import GraphNode as Node
from collections import deque, OrderedDict


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        if not node.neighbors:
            return Node(node.val)

        dq = deque([node])

        adj_matrix = []
        visited = set()
        created = OrderedDict()

        while dq:
            cur = dq.popleft()
            if not cur.val in created:
                created[cur.val] = Node(cur.val)

            if cur not in visited:
                temp = []
                for neighbor in cur.neighbors:
                    if not neighbor.val in created:
                        created[neighbor.val] = Node(neighbor.val)
                    temp.append(neighbor.val)
                    dq.append(neighbor)
                adj_matrix.append(temp)

                visited.add(cur)

        for i, new_node in enumerate(created.values()):
            for val in adj_matrix[i]:
                new_node.neighbors.append(created[val])

        return created[node.val]


tl = Node(1)
tr = Node(2)
br = Node(3)
bl = Node(4)

tl.neighbors = [tr, bl]
tr.neighbors = [tl, br]
bl.neighbors = [tl, br]
br.neighbors = [tr, bl]

tl.print_all_nodes()
print("-" * 40)
Solution().cloneGraph(tl).print_all_nodes()
