class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        cur = []
        res = []

        def back(left: int, right: int):
            if left == right == 0:
                res.append("".join(cur))
            if left != 0:
                cur.append("(")
                back(left - 1, right)
                cur.pop()
            if right > left:
                cur.append(")")
                back(left, right - 1)
                cur.pop()

        back(n, n)
        return res


s = Solution()
tests = [
    # 1,
    # 2,
    3,
]

for test in tests:
    print(s.generateParenthesis(test))
