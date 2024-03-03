# import sys
# from collections import defaultdict


# class Node:
#     def __init__(self):
#         self.children = defaultdict(Node)
#         self.popularity = -1
#         self.word = -1


# class Trie:
#     def __init__(self):
#         self.root = Node()

#     def insert(self, word, popularity, index):
#         node = self.root
#         for ch in word:
#             node = node.children[ch]
#             if node.popularity < popularity:
#                 node.popularity = popularity
#                 node.word = index

#     def query(self, prefix):
#         node = self.root
#         for ch in prefix:
#             if ch not in node.children:
#                 return -1
#             node = node.children[ch]
#         return node.word


# def solve():
#     trie = Trie()
#     words = []
#     for i in range(n):
#         word, popularity = input().split()
#         popularity = int(popularity)
#         words.append(word)
#         trie.insert(word, popularity, i + 1)
#     t = ""
#     for _ in range(q):
#         query = input().strip().split()
#         if query[0] == "+":
#             t += query[1]
#         else:
#             t = t[:-1]
#         print(trie.query(t))


# if __name__ == "__main__":
#     solve()


class TrieNode:
    def __init__(self, popularity=None):
        self.children = {}
        self.popularity = popularity
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, popularity):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.popularity = popularity
        node.end = True

    def _walk_trie(self, node, word, word_list):

        if node.children:
            for char in node.children:
                word_new = word + char
                if node.children[char].end:
                    word_list.append((word_new, node.children[char].popularity))
                self._walk_trie(node.children[char], word_new, word_list)

    def auto_complete(self, prefix):
        node = self.root

        word_list = []

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return word_list

        if node.end:
            word_list.append(prefix)

        self._walk_trie(node, prefix, word_list)
        return word_list


if __name__ == "__main__":
    n, q = map(int, input().split())
    t = Trie()

    words = []
    for i in range(n):
        word, popularity = input().split()
        popularity = int(popularity)
        words.append(word)
        t.insert(word, popularity)

    cur_q = ""
    for _ in range(q):
        query = input().strip().split()
        if query[0] == "+":
            cur_q += query[1]
        else:
            cur_q = cur_q[:-1]

        results = t.auto_complete(cur_q)
        cur_r = (0, -1)
        index = -1

        if not results:
            print(-1)
        else:
            for i, r in enumerate(results):
                if r[1] > cur_r[1]:
                    cur_r = (i, r[1])
                    index = i

        print(i + 1)
