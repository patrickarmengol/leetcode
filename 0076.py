from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t: defaultdict[str, int] = defaultdict(int)
        count_sliding: defaultdict[str, int] = defaultdict(int)

        smallest = ""

        # initialize count_t
        for c in t:
            count_t[c] += 1

        # start sliding window
        have = 0
        need = len(count_t)
        i, j = 0, 0
        while True:
            # extend right until count for each char >=
            while have != need:
                # end when right goes past end
                if j == len(s):
                    return smallest
                # update sliding count and check
                if s[j] in count_t:
                    count_sliding[s[j]] += 1
                    if count_sliding[s[j]] == count_t[s[j]]:
                        have += 1
                j += 1
            # retract left until count for any char <
            while have == need:
                # check for new smallest substr
                if (j - i) <= len(smallest) or smallest == "":
                    smallest = s[i:j]
                # update sliding count and check
                if s[i] in count_t:
                    if count_sliding[s[i]] == count_t[s[i]]:
                        have -= 1
                    count_sliding[s[i]] -= 1
                i += 1


s = Solution()
tests = [
    ("ADOBECODEBANC", "ABC"),
    ("a", "a"),
    ("a", "aa"),
]
for test in tests:
    print(s.minWindow(test[0], test[1]))
