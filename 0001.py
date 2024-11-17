class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {n: i for i, n in enumerate(nums)}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in d and d[diff] != i:
                return [i, d[diff]]
        assert False
