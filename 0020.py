class Solution:
    def isValid(self, s: str) -> bool:
        blah = []
        for c in s:
            if c in "({[":
                blah.append(c)
            else:
                if not blah:
                    return False
                pp = blah.pop()
                if pp + c not in "(){}[]":
                    return False
        return len(blah) == 0
