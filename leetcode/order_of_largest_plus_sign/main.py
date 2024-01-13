class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # finding the square with uneven n, where we can place the "+" sign
        start = [0, 0]  # top left cell
        end = [n - 1, n - 1]  # bottom right cell
        for mine in mines:
            # if the mine is in the center of the grid
            if mine[0] == mine[1] == n // 2:
                # find an appropriate corner with
                ...
            # if the mine is on the center row of the grid
            if mine[0] == n // 2:
                # remove the column
                if mine[1] > n // 2:
                    new_end = [mine[1] - 1, mine[1] - 1]
                    end = new_end if new_end[1] < end[1] else end
                else:
                    new_start = [mine[1] + 1, mine[1] + 1]
                    end = new_end if new_end < end else end
                ...
            # if the mine is on the center column of the grid
            if mine[1] == n // 2:
                # remove the row
                ...
