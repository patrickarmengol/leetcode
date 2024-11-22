class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        def steps(t: int, p: int, s: int) -> float:
            # calculates steps to target
            # tp = ip + speed * steps
            # steps = (tp - ip)/speed
            return float(t - p) / s

        ps = sorted(
            zip(position, speed, [steps(target, x, y) for x, y in zip(position, speed)])
        )
        count = 0
        while ps:
            popped = ps.pop()
            while ps and (
                popped[2] > ps[-1][2] or abs(popped[2] - ps[-1][2]) < 0.0000001
            ):
                ps.pop()
            count += 1

        return count


s = Solution()
tests = [
    (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),
    (10, [3], [3]),
    (10, [0, 4, 2], [2, 1, 3]),
]
for test in tests:
    print(s.carFleet(test[0], test[1], test[2]))
