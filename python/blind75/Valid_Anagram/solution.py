from collections import defaultdict
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        dict = defaultdict(int)

        for c in s: dict[c] += 1
        for c in t: dict[c] -= 1

        return all(x == 0 for x in dict.values())

    def isAnagram2(self, s: str, t: str) -> bool:
        dict = {}
        
        if len(s) != len(t):
            return False

        for (l, r) in zip(s, t):
            if l in dict:
                dict[l] += 1
                if dict[l] == 0:
                   dict.pop(l) 
            else:
                dict[l] = 1
            
            if r in dict:
                dict[r] -= 1
                if dict[r] == 0:
                   dict.pop(r) 
            else:
                dict[r] = -1

        return True if len(dict) == 0 else False
        