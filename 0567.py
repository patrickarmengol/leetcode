class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # initialize s1 count
        count_s1 = [0] * 26
        for c in s1:
            count_s1[ord(c) - ord("a")] += 1

        # initialize sliding count
        count_sliding = [0] * 26
        for c in s2[0 : len(s1)]:
            count_sliding[ord(c) - ord("a")] += 1
        if count_sliding == count_s1:
            return True

        # iterate through rest of s2, updating and checking counts
        for i in range(len(s1), len(s2)):
            count_sliding[ord(s2[i]) - ord("a")] += 1
            count_sliding[ord(s2[i - len(s1)]) - ord("a")] -= 1
            if count_sliding == count_s1:
                return True

        return False


s = Solution()
tests = [
    ("ab", "eidbaooo"),
    ("ab", "eidboaoo"),
]
for test in tests:
    print(s.checkInclusion(test[0], test[1]))
