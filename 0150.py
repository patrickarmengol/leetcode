class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s = []
        for token in tokens:
            match token:
                case "+":
                    b = s.pop()
                    a = s.pop()
                    s.append(a + b)
                case "-":
                    b = s.pop()
                    a = s.pop()
                    s.append(a - b)
                case "*":
                    b = s.pop()
                    a = s.pop()
                    s.append(a * b)
                case "/":
                    b = s.pop()
                    a = s.pop()
                    s.append(int(a / b))
                case _:
                    s.append(int(token))
        return s[-1]


s = Solution()
tests = [
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
]

for test in tests:
    print(s.evalRPN(test))
