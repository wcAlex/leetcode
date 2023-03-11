
# for counting chars, we could use array (with char value as index) instead of dictionary for efficiency. 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 30

        for c in magazine:
            arr[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            arr[ord(c) - ord('a')] -= 1
            if arr[ord(c) - ord('a')] < 0:
                return False
        
        return True