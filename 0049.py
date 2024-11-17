from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d: defaultdict[str, list[str]] = defaultdict(list)
        for s in strs:
            a = [0] * 26
            for c in s:
                a[ord(c) - ord("a")] += 1
            d[str(a)].append(s)

        return list(d.values())
