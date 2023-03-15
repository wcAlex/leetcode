from typing import List

class Solution:
    # The intuition behind this code is here:
    # https://leetcode.com/problems/maximum-subarray/solutions/20193/dp-solution-some-thoughts/
    # great explaination
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)
        dp[0], max_sum = nums[0], nums[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
            max_sum = max(max_sum, dp[i])

        return max_sum
    
    # a simpler version
    def maxSubArray2(self, nums: List[int]) -> int:
        
        cur_opt, max_sum = nums[0], nums[0]

        for i in range(1, len(nums)):
            cur_opt = max(nums[i] + cur_opt, nums[i])
            max_sum = max(max_sum, cur_opt)

        return max_sum
