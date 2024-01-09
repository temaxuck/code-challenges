class RecursiveImplementation:
    @staticmethod
    def DFS(graph, start, end, visited=[]):
        print(start, end, visited)
        if start == end:
            return True
        try:
            if end in graph[start]:
                return True

            for node in graph[start]:
                if node in visited:
                    continue
                visited.append(node)
                if RecursiveImplementation.DFS(graph, node, end, visited):
                    return True

            return False
        except KeyError:
            return False


def get_graph(seed: int = 0):
    if seed % 2 == 0:
        return {
            "a": ["b"],
            "b": ["c", "d", "e", "f", "g"],
            "g": ["h"],
            "h": ["i", "j"],
        }
    else:
        return {
            "a": ["b", "e"],
            "b": ["a", "f", "c"],
            "c": ["b", "g", "d"],
            "d": ["c", "h"],
            "e": ["a", "f", "i"],
            "f": ["e", "b", "g", "j"],
            "g": ["f", "c", "h", "k"],
            "h": ["d", "g", "l"],
            "i": ["e", "j", "k"],
            "j": ["i", "f", "k", "n"],
            "k": ["j", "g", "l", "o"],
            "l": ["h", "k", "p"],
            "m": ["i", "n", "q"],
            "n": ["m", "j", "o", "r"],
            "o": ["n", "k", "p", "s"],
            "p": ["l", "o", "t"],
            "q": ["m", "r"],
            "r": ["q", "n", "s"],
            "s": ["r", "o", "t"],
            "t": ["s", "p"],
        }


if __name__ == "__main__":
    print(RecursiveImplementation.DFS(get_graph(), "c", "i"))
