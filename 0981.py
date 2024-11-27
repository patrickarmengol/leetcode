from collections import defaultdict
import bisect
from operator import itemgetter


class TimeMap:
    def __init__(self):
        self.d: defaultdict[str, list[tuple[int, str]]] = defaultdict(
            list[tuple[int, str]]
        )

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        a = self.d[key]
        b = bisect.bisect_right(a, timestamp, key=itemgetter(0))
        if b == 0:
            return ""
        return a[b - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
