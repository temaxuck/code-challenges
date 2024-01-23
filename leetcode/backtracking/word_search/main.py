from typing import List


class Solution:
    def get_character_at(self, board, point):
        r, c = point

        try:
            return board[r][c]
        except IndexError:
            return None

    def find_char_adjacent_to(self, board, point, char):
        m, n = len(board), len(board[0])
        res = []
        row, col = point

        t = (row - 1, col) if 0 <= row - 1 < m else None
        b = (row + 1, col) if 0 <= row + 1 < m else None
        l = (row, col - 1) if 0 <= col - 1 < n else None
        r = (row, col + 1) if 0 <= col + 1 < n else None

        for p in [t, b, l, r]:
            if p and p not in self.visited and self.get_character_at(board, p) == char:
                res.append(p)

        return res

    def find_char(self, board, char):
        for r in range(m):
            for c in range(n):
                if board[r][c] == char:
                    return r, c

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        word_len = len(word)
        self.visited = set()

        def dfs(i, point):
            self.visited.add(point)

            if i >= word_len:
                return True
            for p in self.find_char_adjacent_to(board, point, word[i]):
                if dfs(i + 1, p):
                    return True
                self.visited.remove(p)

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(1, (r, c)):
                        return True
                    self.visited.remove((r, c))

        return False


# Passed
# print(
#     Solution().exist(
#         [
#             ["F", "R", "D", "R"],
#             ["E", "A", "D", "F"],
#         ],
#         "RFEADFRD",
#     )
# )

# Passed
# print(
#     Solution().exist(
#         [
#             ["C", "A", "A"],
#             ["A", "A", "A"],
#             ["B", "C", "D"],
#         ],
#         "AAB",
#     )
# )


# Passed
print(
    Solution().exist(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ],
        "SEEA",
    )
)
