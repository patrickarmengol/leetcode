class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        level = 0
        total = 0
        while left < right:
            count_left = 0
            while left < right and height[left] <= level:
                count_left += level - height[left]
                left += 1

            count_right = 0
            while left < right and height[right] <= level:
                count_right += level - height[right]
                right -= 1

            total += count_left + count_right
            level += 1

        return total


s = Solution()
tests = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5],
]
for test in tests:
    print(s.trap(test))
