class Solution1:
    nums_map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

    def romanToInt(self, s: str) -> int:
        res = 0

        for i, c in enumerate(s):
            v = Solution1.nums_map[c]
            if i < len(s)-1:
                if v < Solution1.nums_map[s[i+1]]:
                    res -= v
                    continue
            
            res += v

        return res

        

        