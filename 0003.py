class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        longest = 0
        u = set()
        while j < len(s):
            while s[j] in u:
                u.remove(s[i])
                i += 1
            u.add(s[j])
            longest = max(longest, len(u))
            j += 1
        return longest


s = Solution()
tests = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
]
for test in tests:
    print(s.lengthOfLongestSubstring(test))
