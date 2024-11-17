class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)

        px = 1
        for i in range(len(nums)):
            pre[i] = px
            px *= nums[i]

        sx = 1
        for i in range(len(nums) - 1, -1, -1):
            suf[i] = sx
            sx *= nums[i]

        return [pre[i] * suf[i] for i in range(len(nums))]


s = Solution()
tests = [
    [1, 2, 3, 4],
    [-1, 1, 0, -3, 3],
]
for test in tests:
    print(s.productExceptSelf(test))


# [1,2,3,4]
# [1,1,2,6]
# [24,12,4,1]
