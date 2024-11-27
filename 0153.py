class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[lo] > nums[hi] and nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]


s = Solution()
tests = [
    [3, 4, 5, 1, 2],
    [4, 5, 6, 7, 0, 1, 2],
    [11, 13, 15, 17],
    [2, 1],
]

for test in tests:
    print(s.findMin(test))
