class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        tmp = ""

        for c in s:
            if c.isalnum():
                tmp += c
        return tmp == tmp[::-1]
