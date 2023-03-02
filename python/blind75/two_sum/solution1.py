class SolutionA:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}

        for idx, val in enumerate(nums):
            remain = target - val
            if remain in dict:
                return [dict[remain], idx]
            dict[val] = idx

        return []