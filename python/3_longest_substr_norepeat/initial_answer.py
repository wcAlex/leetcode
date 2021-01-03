class Solution:
    def lengthOfLongestSubstring_Old(self, s: str) -> int:
        
        cnt, res, head, last = 0, 0, 0, 0
        sub = set()
        while last < len(s):
            
            if s[last] not in sub:
                sub.add(s[last])
                cnt += 1
                last += 1
                res = cnt if cnt > res else res
                
                continue
                
            while head < last and s[head] != s[last]:
                sub.remove(s[head])
                head += 1
                cnt -= 1
                
            head += 1
            last += 1
                    
        return res

    # A good sliding window approach, only one loop.
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest, left, right = 0, 0, 0
        chars = set()
        while left < len(s) and right <len(s):
            
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(s[left])
                left += 1        
            
        return longest

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("abba"))
print(sol.lengthOfLongestSubstring(""))