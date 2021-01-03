class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        cnt, b = 0, 0
        dct = {}
        
        for i, v in enumerate(s):
            if v in dct:
                b = max(b, dct[v] + 1)
            
            dct[v] = i
            cnt = max(cnt, i-b+1)
        
        return cnt
            
                
sol = Solution()
# print(sol.lengthOfLongestSubstring("abcabcbb"))
# print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("abba"))
print(sol.lengthOfLongestSubstring(""))