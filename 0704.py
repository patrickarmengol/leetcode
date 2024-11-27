import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(nums) or nums[lo] != target:
            return -1
        return lo

    def search_builtin(self, nums: list[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)
        if i == len(nums) or nums[i] != target:
            return -1
        return i
