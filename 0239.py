from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res: list[int] = []
        q: deque[int] = deque()
        i, j = 0, 0

        while j < len(nums):
            # pop from end of monotonic queue to fit new elem
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)

            # pop from start of monotonic queue til in range of window
            while i > q[0]:
                q.popleft()

            # add front of monotonic queue to result and slide window
            if j >= k - 1:
                res.append(nums[q[0]])
                i += 1
            j += 1

        return res


s = Solution()
tests = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3),
    ([1, -1], 1),
]
for test in tests:
    print(s.maxSlidingWindow(test[0], test[1]))
