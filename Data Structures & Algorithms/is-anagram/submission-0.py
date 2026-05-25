class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alpha = [0] * 26

        for i in range(len(s)):
            alpha[ord(s[i]) - 97] += 1
            alpha[ord(t[i]) - 97] -= 1

        if alpha.count(0) != 26:
            return False
        
        return True