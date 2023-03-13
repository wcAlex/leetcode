class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        bucket = []

        for n in nums:
            if len(bucket) == 0 or bucket[-1] == n:
                bucket.append(n)
            else:
                bucket.pop()
        
        return bucket[-1]
    
    def majorityElement2(self, nums: list[int]) -> int:
        b, e, cnt = 0, len(nums) - 1, 0

        while b < e:
            if nums[b] == nums[e]:
                cnt += 1
            else:
                if cnt == 0:
                    b += 1
                else:
                    cnt -= 1
            e -= 1

        return nums[b]
    
    # another efficient algorithm is the VOTing:
    # // Moore voting algorithm
    # public int majorityElement3(int[] nums) {
    #     int count=0, ret = 0;
    #     for (int num: nums) {
    #         if (count==0)
    #             ret = num;
    #         if (num!=ret)
    #             count--;
    #         else
    #             count++;
    #     }
    #     return ret;
    # }

