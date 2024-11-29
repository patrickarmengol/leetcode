from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        longest = 0  # longest stretch
        highest_freq = 0  # num of most freq char
        count = defaultdict(int)

        while j < len(s):
            # update count of char under right pointer and update highest_freq
            count[s[j]] += 1
            highest_freq = max(highest_freq, count[s[j]])

            # adjust window until valid (window size - highest_freq <= k)
            while (j - i + 1) - highest_freq > k:
                count[s[i]] -= 1
                i += 1

            # update longest stretch and increment right pointer
            longest = max(longest, j - i + 1)
            j += 1

        return longest
