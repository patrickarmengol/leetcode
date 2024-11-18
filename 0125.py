class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s))
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
