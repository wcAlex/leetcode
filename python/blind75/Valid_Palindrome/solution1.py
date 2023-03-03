class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ c for c in s.lower() if c.isalnum()]

        return s == s[::-1]


    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s)-1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        
        return True
                