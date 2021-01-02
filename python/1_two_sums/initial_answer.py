# another person's post on sum questions summary, ex: 3 sum, 4 sum ...
# https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        
        for i, v in enumerate(nums):
            c = target -v
            if c in dct:
                return [dct[c], i]
            else:
                dct[v] = i
        
        return []
    