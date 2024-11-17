from collections import Counter, defaultdict
from operator import itemgetter


# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         return [x for (x, _) in Counter(nums).most_common(k)]


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # counter
        d: defaultdict[int, int] = defaultdict(int)
        for n in nums:
            d[n] += 1

        # buckets for each possible count (max is len of nums)
        a = [[] for _ in range(len(nums))]
        for n, c in d.items():
            a[c - 1].append(n)

        # flatten and iterate in reverse for k elems
        return [y for x in a for y in x][::-1][:k]


s = Solution()
tests = [([1, 1, 1, 2, 2, 3], 2)]

for t in tests:
    print(s.topKFrequent(t[0], t[1]))
