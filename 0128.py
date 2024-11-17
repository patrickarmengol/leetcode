class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        longest = 0

        for n in s:
            if n - 1 not in s:
                # found a start
                count = 1
                while n + count in s:
                    count += 1
                longest = max(longest, count)

        return longest
