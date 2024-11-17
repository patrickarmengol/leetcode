from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # hashmap of sets for each direction
        rows: defaultdict[int, set[str]] = defaultdict(set)
        cols: defaultdict[int, set[str]] = defaultdict(set)
        boxes: defaultdict[tuple[int, int], set[str]] = defaultdict(set)

        # iterate through board
        for r in range(9):
            for c in range(9):
                tile = board[r][c]
                # skip irrelevant
                if tile == ".":
                    continue
                # check if already seen
                elif (
                    tile in rows[r]
                    or tile in cols[c]
                    or tile in boxes[(r // 3, c // 3)]
                ):
                    return False
                # add to seen
                else:
                    rows[r].add(tile)
                    cols[c].add(tile)
                    boxes[(r // 3, c // 3)].add(tile)
        return True


s = Solution()
tests = [
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ],
]

for test in tests:
    print(s.isValidSudoku(test))
