class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = "".join(c for c in s if c.isalnum())
        s = s.lower()
        for i in range((len(s) // 2)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True