import bisect, math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # consider k = 1..max(piles)
        lo = 1
        hi = max(piles)

        # bisect_left with comparator reversed (since total_hours descends as k ascends)
        while lo < hi:
            k = (lo + hi) // 2
            total_hours = sum(math.ceil(n / k) for n in piles)
            if total_hours > h:
                lo = k + 1
            else:
                hi = k
        return lo


s = Solution()
tests = [
    ([3, 6, 7, 11], 8),
    ([30, 11, 23, 4, 20], 5),
    ([30, 11, 23, 4, 20], 6),
]
for test in tests:
    print(s.minEatingSpeed(test[0], test[1]))
