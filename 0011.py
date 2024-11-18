class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        largest = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            largest = max(largest, area)

            # could just move pointers over 1 here, but this skips calc area for worse heights
            if height[left] > height[right]:
                last_rh = height[right]
                while right > left and last_rh >= height[right]:
                    right -= 1
            else:
                last_lh = height[left]
                while left < right and last_lh >= height[left]:
                    left += 1

        return largest


s = Solution()
tests = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
]
for test in tests:
    print(s.maxArea(test))
