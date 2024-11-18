class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        snums = sorted(nums)
        res: set[tuple[int, int, int]] = set()

        for i in range(len(snums)):
            # avoid adding 3 positive numbers
            if snums[i] > 0:
                break
            # skip duplicate numbers for i pointer
            if i > 0 and snums[i - 1] == snums[i]:
                continue
            # two pointer for remaining sum
            left = i + 1
            right = len(snums) - 1
            while left < right:
                total = snums[i] + snums[left] + snums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.add((snums[i], snums[left], snums[right]))
                    left += 1
                    right -= 1
        return [list(a) for a in res]


s = Solution()
tests = [
    [-1, 0, 1, 2, -1, -4],
    [0, 1, 1],
    [0, 0, 0],
]
for test in tests:
    print(s.threeSum(test))
