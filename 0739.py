class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        s: list[tuple[int, int]] = []
        for i, t in enumerate(temperatures):
            while s and s[-1][0] < t:
                p = s.pop()
                res[p[1]] = i - p[1]
            s.append((t, i))
        return res
