class Solution:
    # 8^^^whatever

    def encode(self, strs: list[str]) -> str:
        es: list[str] = []
        for s in strs:
            es.append(f"{len(s)}^^^{s}")
        return "".join(es)

    def decode(self, s: str) -> list[str]:
        ds: list[str] = []
        while s != "":
            print(s)
            dp = s.find("^^^")
            ls = int(s[:dp])
            ss = s[dp + 3 : dp + 3 + ls]
            ds.append(ss)
            s = s[dp + 3 + ls :]
        return ds


s = Solution()
tests = [
    ["neet", "code", "love", "you"],
]
for test in tests:
    encoded = s.encode(test)
    print(encoded)
    print(s.decode(encoded))
