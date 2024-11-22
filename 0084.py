class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        s: list[tuple[int, int]] = []
        largest = 0
        for i, h in enumerate(heights):
            ni = i
            while s and s[-1][0] >= h:
                p = s.pop()
                largest = max(largest, (i - p[1]) * p[0])
                ni = p[1]
            s.append((h, ni))
        while s:
            p = s.pop()
            largest = max(largest, (len(heights) - p[1]) * p[0])
        return largest


s = Solution()
tests = [
    [2, 1, 5, 6, 2, 3],
    [2, 4],
]
for test in tests:
    print(s.largestRectangleArea(test))
