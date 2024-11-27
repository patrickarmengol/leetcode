class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if target == nums[mid]:
                return mid

            if nums[lo] <= nums[mid]:  # left sector
                if (
                    nums[mid] < target or nums[lo] > target
                ):  # target not between lo and mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:  # right sector
                if (
                    nums[mid] > target or nums[hi] < target
                ):  # target not between mid and hi
                    hi = mid - 1
                else:
                    lo = mid + 1

        return -1


# [4, 5, 6, 7, 0, 1, 2]


s = Solution()
tests = [
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([4, 5, 6, 7, 0, 1, 2], 3),
    ([1], 0),
    ([1, 3], 3),
]
for test in tests:
    print(s.search(test[0], test[1]))
