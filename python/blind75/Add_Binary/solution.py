class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            return self.addBinary(b, a)

        res, add, cur_a, cur_b = "", 0, len(a)-1, len(b)-1
        while cur_a >= 0:
            val = int(a[cur_a])
            if cur_b >= 0:
                val += int(b[cur_b])
            val += add

            cur_a -= 1
            cur_b -= 1

            add = int(val/2)
            val = val % 2
            res = str(val) + res
        
        if add > 0:
            res = "1" + res

        return res
    
    # a more concised version
    # don't think which array is longer
    def addBinary2(self, a: str, b: str) -> str:
        res, i, j, carry = "", len(a)-1, len(b)-1, 0

        while i>=0 or j>=0:
            val = carry
            if i >= 0: val += int(a[i])
            if j >= 0: val += int(b[j])

            i, j = i-1, j-1

            res = str(val%2) + res
            carry = val // 2

        return res if carry == 0 else "1"+res

    # a faster version
    def addBinary3(self, a: str, b: str) -> str:
        res, i, j, carry = "", len(a)-1, len(b)-1, 0

        while i>=0 or j>=0:
            val = carry
            if i >= 0: val += int(a[i])
            if j >= 0: val += int(b[j])

            i, j = i-1, j-1

            # just append and reverse at the end, which make things faster
            res += str(val%2)
            carry = val // 2

        if carry != 0: res += "1"
        return res[::-1]

