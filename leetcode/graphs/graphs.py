from collections import deque


class GraphNode:
    def __init__(self, val=0, neighbors=None):
        if not neighbors:
            neighbors = []

        self.val = val
        self.neighbors = neighbors

    def __str__(self):
        return f"GraphNode({self.val})"

    def __repr__(self):
        return f"GraphNode({self.val})"

    def print_all_nodes(self):
        dq = deque([self])
        visited = set()

        while dq:
            node = dq.popleft()

            if node not in visited:
                visited.add(node)
                print(node)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    dq.append(neighbor)
