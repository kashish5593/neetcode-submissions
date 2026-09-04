class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, i = 0, len(s) - 1

        while l < i:
            while l < i and not self.alphaNum(s[l]):
                l += 1
            while i > l and not self.alphaNum(s[i]):
                i -= 1
            if s[l].lower() != s[i].lower():
                return False
            l, i = l + 1, i - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))