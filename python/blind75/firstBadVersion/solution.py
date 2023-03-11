# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        b, e = 1, n

        while b <= e:
            m = b + int((e-b)/2)

            if isBadVersion(m):
                e = m-1
            else: 
                b = m + 1
            
        return e+1