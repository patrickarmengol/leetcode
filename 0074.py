import bisect


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rowb = bisect.bisect_right([a[0] for a in matrix], target) - 1
        colb = bisect.bisect_left(matrix[rowb], target)
        return colb != len(matrix[rowb]) and matrix[rowb][colb] == target


s = Solution()
tests = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
]
for test in tests:
    print(s.searchMatrix(test[0], test[1]))
